from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from core.validators import validate_phone_digits


User = get_user_model()


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True,
        validators=[validate_phone_digits],
    )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_country = CountryField(
        default='GB', editable=False,
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class ContactMessage(models.Model):
    """
    Model to store contact messages from users
    """
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In progress"),
        ("resolved", "Resolved"),
    ]

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    subject = models.CharField(max_length=150)
    message = models.TextField()

    order_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    response = models.TextField(blank=True)
    responded_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Customer queries"

    def __str__(self):
        return f"{self.subject} ({self.email})"
