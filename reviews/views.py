from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from products.models import Product

from .forms import ReviewForm
from .models import Review
from .utils import user_has_purchased_product


@login_required
def add_review(request, product_id):
    """
    Allow a user to add a review for a product they have purchased.
    One review per user per product.
    """
    product = get_object_or_404(Product, id=product_id)

    if not user_has_purchased_product(request.user, product):
        messages.error(
            request, "You can only review products you’ve purchased."
        )
        return redirect("product_detail", product_id=product.id)

    existing = Review.objects.filter(
        product=product, user=request.user
    ).first()
    if existing:
        messages.info(
            request,
            "You’ve already reviewed this item. You can edit your review."
        )
        return redirect("edit_review", review_id=existing.id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.is_approved = False
            review.save()
            messages.success(
                request, "Thanks! Your review has been submitted for approval."
            )
            return redirect("product_detail", product_id=product.id)
        all_reviews = Review.objects.filter(
            product=product
        ).select_related("user")
        context = {
            "product": product,
            "review_form": form,
            "all_reviews": all_reviews,
        }
        return render(request, "products/product_detail.html", context)


@login_required
def edit_review(request, review_id):
    """
    Allow a user to edit their existing review.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product = review.product

    if not user_has_purchased_product(request.user, product):
        messages.error(
            request, "You can only review products you’ve purchased."
        )
        return redirect("product_detail", product_id=product.id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.is_approved = False
            updated.save()
            messages.success(
                request, "Your review was updated and is pending approval."
            )
            return redirect("product_detail", product_id=product.id)
    else:
        form = ReviewForm(instance=review)

    return render(
        request, "reviews/review_form.html",
        {"form": form, "product": product, "is_edit": True}
    )


@login_required
def delete_review(request, review_id):
    """
    Allow a user to delete their existing review.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product_id = review.product_id

    if request.method == "POST":
        review.delete()
        messages.success(request, "Your review was deleted.")
        return redirect("product_detail", product_id=product_id)

    return render(
        request, "reviews/review_confirm_delete.html", {"review": review}
    )
