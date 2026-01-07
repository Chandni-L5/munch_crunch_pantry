from django.utils.cache import add_never_cache_headers


class NoStoreCheckoutPagesMiddleware:
    """
    Prevent browsers from caching checkout-related pages
    so Back won't resurrect them.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith(("/checkout/", "/basket/")):
            add_never_cache_headers(response)

        return response
