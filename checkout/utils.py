from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_confirmation_email(order, request):
    cust_email = order.email

    if order.user_profile:
        base_url = reverse("order_history", args=[order.order_number])
    else:
        base_url = reverse("checkout_success", args=[order.order_number])

    order_url = request.build_absolute_uri(f"{base_url}?from_email=1")

    subject = render_to_string(
        "checkout/confirmation_emails/confirmation_email_subject.txt",
        {"order": order},
    ).strip()

    body = render_to_string(
        "checkout/confirmation_emails/confirmation_email_body.txt",
        {
            "order": order,
            "contact_email": settings.DEFAULT_FROM_EMAIL,
            "order_url": order_url,
        },
    )

    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])
