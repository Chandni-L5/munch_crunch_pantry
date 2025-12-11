from django.contrib import admin
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("user_profile", "subject", "email", "order_number", "status", "created_at", "responded_at")
    list_filter = ("status", "created_at")
    search_fields = ("user_profile__user__username", "email", "subject", "order_number", "message", "response")
    readonly_fields = ("created_at", "responded_at")
    fields = ("user_profile", "subject", "email", "order_number", "message", "status", "response", "created_at", "responded_at")

    def save_model(self, request, obj, form, change):
        send_response_email = (
            "response" in form.changed_data and bool(obj.response.strip())
        )

        if send_response_email:
            obj.responded_at = timezone.now()
            if obj.status != "resolved":
                obj.status = "resolved"

        super().save_model(request, obj, form, change)

        if send_response_email:
            subject = f"[Munch Crunch Pantry] Reply to your query: {obj.subject}"
            message_body = render_to_string(
                "profiles/contact_emails/contact_message_response_email.txt",
                {
                    "contact_message": obj,
                },
            )

            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                [obj.email],
                fail_silently=False
            )
