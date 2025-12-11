from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from home.forms import ContactForm
from products.models import Product
from profiles.models import UserProfile, ContactMessage

import random
import logging


def index(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    random_products = products[:6]
    new_arrivals = Product.objects.order_by('-created_at')[:6]

    context = {
        'products': random_products,
        'new_arrivals': new_arrivals,
    }

    return render(request, 'home/index.html', context)


def shipping(request):
    context = {
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'standard_delivery': settings.STANDARD_DELIVERY,
    }
    return render(request, 'home/shipping.html', context)


def faq(request):
    return render(request, 'home/faq.html')


def returns(request):
    return render(request, 'home/returns.html')


logger = logging.getLogger(__name__)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            user_email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            order_number = form.cleaned_data.get("order_number")

            email_subject = f"[Contact] {subject}"
            if order_number:
                email_subject += f" (Order: {order_number})"

            body_lines = [
                f"Name: {name}",
                f"Email: {user_email}",
            ]
            if order_number:
                body_lines.append(f"Order number: {order_number}")
            body_lines.append("")
            body_lines.append("Message:")
            body_lines.append(message)

            email_body = "\n".join(body_lines)
            to_email = getattr(settings, "SUPPORT_EMAIL", settings.DEFAULT_FROM_EMAIL)

            try:
                email = EmailMessage(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [to_email],
                    reply_to=[user_email],
                )
                email.send(fail_silently=False)
            except Exception as e:
                logger.error(f"Failed to send contact email: {e}")
                messages.error(request, "An error occurred while sending your message. Please try again later.")
            else:
                if request.user.is_authenticated:
                    try:
                        user_profile = UserProfile.objects.get(user=request.user)
                    except UserProfile.DoesNotExist:
                        user_profile = None

                    if user_profile:
                        ContactMessage.objects.create(
                            user_profile=user_profile,
                            subject=subject,
                            message=message,
                            order_number=order_number or "",
                            email=user_email,
                        )
                return redirect('contact_success')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        initial = {}
        if request.user.is_authenticated:
            initial["name"] = request.user.get_full_name() or request.user.username
            initial["email"] = request.user.email
        form = ContactForm(initial=initial)

    return render(request, "home/contact.html", {"form": form})


def contact_success(request):
    return render(request, 'home/contact_success.html')
