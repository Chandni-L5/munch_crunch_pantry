from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.db.models import (
    Avg, Count, Q, Value, FloatField, IntegerField, Min, Sum
)
from django.db.models.functions import Coalesce

from home.forms import ContactForm
from products.models import Product
from profiles.models import UserProfile, ContactMessage
from stories.models import Story

import random
import logging


def about_us(request):
    origin_stories = (
        Story.objects
        .filter(is_published=True)
        .order_by("-created_at")[:4]
    )

    return render(request, "home/about_us.html", {
        "stories": origin_stories,
    })


def index(request):
    base_qs = Product.objects.annotate(
        lowest_price_value=Min("quantities__price"),
        reviews_avg=Coalesce(
            Avg("reviews__rating", filter=Q(reviews__is_approved=True)),
            Value(0.0),
            output_field=FloatField(),
        ),
        reviews_count=Coalesce(
            Count(
                "reviews", filter=Q(reviews__is_approved=True),
                distinct=True
            ),
            Value(0),
            output_field=IntegerField(),
        ),
        total_sold=Coalesce(
            Sum("quantities__orderlineitem__quantity", distinct=True),
            Value(0),
            output_field=IntegerField(),
        ),
    )

    most_sold = base_qs.order_by("-total_sold")[:6]
    new_arrivals = base_qs.order_by("-created_at")[:6]

    context = {
        "most_sold": most_sold,
        "new_arrivals": new_arrivals,
    }
    return render(request, "home/index.html", context)


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
            to_email = getattr(
                settings, "SUPPORT_EMAIL", settings.DEFAULT_FROM_EMAIL
            )

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
                messages.error(
                    request,
                    "An error occurred while sending your message. "
                    "Please try again later."
                )
            else:
                if request.user.is_authenticated:
                    try:
                        user_profile = UserProfile.objects.get(
                            user=request.user
                        )
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
            initial["name"] = (
                request.user.get_full_name() or request.user.username
            )
            initial["email"] = request.user.email
        form = ContactForm(initial=initial)

    return render(request, "home/contact.html", {"form": form})


def contact_success(request):
    return render(request, 'home/contact_success.html')


def about(request):
    return render(request, 'home/about_us.html')


def privacy_policy(request):
    return render(request, 'home/privacy.html')


def terms_of_service(request):
    return render(request, 'home/terms_of_service.html')
