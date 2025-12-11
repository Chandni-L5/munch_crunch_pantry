from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("user_profile", "subject", "email", "order_number", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user_profile__user__username", "email", "subject", "order_number", "message")
