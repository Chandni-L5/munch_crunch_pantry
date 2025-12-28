from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import UserProfile, ContactMessage

User = get_user_model()


class UserProfileAndContactMessageModelTests(TestCase):
    """
    Tests for UserProfile (including post_save signal)
    and ContactMessage models.
    """

    def test_user_profile_is_auto_created_when_user_is_created(self):
        """
        Creating a User should automatically create
        a linked UserProfile via signal.
        """
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123",
        )
        self.assertTrue(UserProfile.objects.filter(user=user).exists())
        self.assertEqual(user.userprofile.user, user)

    def test_user_profile_str_returns_username(self):
        """
        UserProfile __str__ should return the related user's username.
        """
        user = User.objects.create_user(
            username="chandni",
            email="chandni@example.com",
            password="password123",
        )
        self.assertEqual(str(user.userprofile), "chandni")

    def test_contact_message_defaults_and_str_format(self):
        """
        ContactMessage should default status to
        'new' and format __str__ correctly.
        """
        user = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="password123",
        )
        msg = ContactMessage.objects.create(
            user_profile=user.userprofile,
            subject="Delivery question",
            message="Where is my order?",
            email="user1@example.com",
        )
        self.assertEqual(msg.status, "new")
        self.assertEqual(str(msg), "Delivery question (user1@example.com)")

    def test_contact_message_allows_optional_fields_blank(self):
        """
        Optional fields (user_profile, order_number, email) can be blank/null.
        """
        msg = ContactMessage.objects.create(
            subject="General enquiry",
            message="Just saying hi!",
        )
        self.assertIsNone(msg.user_profile)
        self.assertIsNone(msg.order_number)
        self.assertIsNone(msg.email)
        self.assertIsNotNone(msg.created_at)
