from django.shortcuts import render


def handler404(request, exception):
    """
    Custom 404 error handler.
    Renders a user-friendly 404 error page.
    """
    return render(request, 'errors/404.html', status=404)
