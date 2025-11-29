from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q, Min
from django.db.models.functions import Lower
from .models import Category, Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    sort = (request.GET.get('sort') or '').lower() or None
    direction = (request.GET.get('direction') or '').lower() or None
    sortkey = None

    if request.GET:

        # Sorting
        if sort:
            if sort == 'name':
                products = products.annotate(name_lower=Lower('name'))
                sortkey = 'name_lower'
            elif sort == 'category':
                products = products.annotate(category_name_lower=Lower('category__name'))
                sortkey = 'category_name_lower'
            elif sort == 'price':
                products = products.annotate(min_price=Min('quantities__price'))
                sortkey = 'min_price'
            if sortkey and direction == 'desc':
                sortkey = f'-{sortkey}'
            if sortkey:
                products = products.order_by(sortkey)

        # Category filtering
        if 'category' in request.GET:
            category_slugs = request.GET['category'].split(',')
            products = products.filter(category__slug__in=category_slugs)
            categories = Category.objects.filter(slug__in=category_slugs)

        # Search bar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}' if sort and direction else ''

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(
        Product.objects.prefetch_related('quantities__quantity'),
        pk=product_id
    )
    return render(request, "products/product_detail.html", {"product": product})
