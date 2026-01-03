from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q, Min, Avg, Count
from django.db.models.functions import Lower

from reviews.models import Review
from reviews.forms import ReviewForm
from reviews.utils import user_has_purchased_product

from .models import Category, Product


def product_detail_legacy(request, product_id):
    """A view to show individual product details using legacy ID URL"""

    product = get_object_or_404(
        Product, pk=product_id
    )
    return redirect('product_detail', slug=product.slug, permanent=True)


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.annotate(
        lowest_price_value=Min("quantities__price")
    )
    query = None
    categories = None

    sort = (request.GET.get("sort") or "").lower() or None
    direction = (request.GET.get("direction") or "").lower() or None
    sortkey = None

    if request.GET:

        # Sorting
        if sort:
            if sort == "name":
                products = products.annotate(name_lower=Lower("name"))
                sortkey = "name_lower"
            elif sort == "category":
                products = products.annotate(
                    category_name_lower=Lower("category__name")
                )
                sortkey = "category_name_lower"
            elif sort == "price":
                sortkey = "lowest_price_value"

            if sortkey and direction == "desc":
                sortkey = f"-{sortkey}"
            if sortkey:
                products = products.order_by(sortkey)

        # Category filtering
        if "category" in request.GET:
            category_slugs = request.GET["category"].split(",")
            products = products.filter(category__slug__in=category_slugs)
            categories = Category.objects.filter(slug__in=category_slugs)

        # Search bar
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))

            queries = Q(
                name__icontains=query
            ) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}" if sort and direction else ""

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    anchor = "#reviews-section"
    all_reviews = Review.objects.filter(product=product).select_related("user")
    approved_reviews = all_reviews.filter(is_approved=True)

    stats = approved_reviews.aggregate(
        avg=Avg("rating"),
        cnt=Count("id"),
    )
    product.rating_avg = stats["avg"] or 0
    product.rating_count = stats["cnt"] or 0

    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            product=product, user=request.user
        ).first()

    has_purchased = (
        request.user.is_authenticated
        and user_has_purchased_product(request.user, product)
    )

    editing = (
        request.user.is_authenticated
        and user_review
        and request.GET.get("edit_review") == "1"
    )

    can_create = (
        request.user.is_authenticated
        and has_purchased
        and user_review is None
    )

    if request.method == "POST" and request.user.is_authenticated:
        action = request.POST.get("action")

        if action == "delete_review" and user_review:
            user_review.delete()
            messages.success(request, "Your review was deleted.")
            return redirect(
                reverse(
                    "product_detail", kwargs={"slug": product.slug}
                ) + anchor
            )

        if action in ("create_review", "update_review") and has_purchased:
            form_instance = user_review if action == "update_review" else None
            form = ReviewForm(request.POST, instance=form_instance)

            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.is_approved = False
                review.save()

                messages.success(
                    request,
                    "Your review was updated and is pending approval."
                    if action == "update_review"
                    else "Thanks! Your review is pending approval."
                )

                return redirect(
                    reverse(
                        "product_detail", kwargs={"slug": product.slug}
                    ) + anchor
                )

    review_form = None
    if can_create:
        review_form = ReviewForm()
    elif editing and user_review:
        review_form = ReviewForm(instance=user_review)

    context = {
        "product": product,
        "all_reviews": all_reviews,
        "user_review": user_review,
        "has_purchased": has_purchased,
        "can_create": can_create,
        "editing": editing,
        "review_form": review_form,
    }
    return render(request, "products/product_detail.html", context)
