from django.shortcuts import render


def handler404(request, exception):
    """
    Custom 404 error handler.
    Renders a user-friendly 404 error page.
    """
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """
    Custom 500 error handler.
    Renders a user-friendly 500 error page.
    """
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception):
    """
    Custom 403 error handler.
    Renders a user-friendly 403 error page.
    """
    return render(request, 'errors/403.html', status=403)


def handler400(request, exception):
    """
    Custom 400 error handler.
    Renders a user-friendly 400 error page.
    """
    return render(request, 'errors/400.html', status=400)
