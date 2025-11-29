from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q, Min
from .models import Category, Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    sortkey = None

    if request.GET:

        # --- Sorting by price ---
        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortkey = sort

            if sort == 'name':
                sortkey = 'name'

            elif sort == 'price':
                products = products.annotate(min_price=Min('quantities__price'))
                sortkey = 'min_price'

        if 'direction' in request.GET and sortkey:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'

        if sortkey:
            products = products.order_by(sortkey)

        # --- Category filtering ---
        if 'category' in request.GET:
            category_slugs = request.GET['category'].split(',')
            products = products.filter(category__slug__in=category_slugs)
            categories = Category.objects.filter(slug__in=category_slugs)

        # --- Search bar function ---
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
