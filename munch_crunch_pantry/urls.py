"""
URL configuration for munch_crunch_pantry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from profiles.views_allauth import RemoveEmail, CustomPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path("accounts/email/", RemoveEmail.as_view(), name="account_email"),
    path(
        "accounts/password/change/",
        CustomPasswordChangeView.as_view(),
        name="account_change_password",
    ),
    path(
        "accounts/password/change/done/",
        TemplateView.as_view(
            template_name="account/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('stories/', include('stories.urls')),
    path('newsletter/', include('newsletter.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = 'munch_crunch_pantry.views.handler404'
handler500 = 'munch_crunch_pantry.views.handler500'
handler403 = 'munch_crunch_pantry.views.handler403'
handler400 = 'munch_crunch_pantry.views.handler400'
