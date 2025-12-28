from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from unittest.mock import patch


class ContactViewTests(TestCase):
    @patch("home.views.EmailMessage.send", side_effect=Exception("boom"))
    def test_contact_shows_error_message_when_email_send_fails(
        self, mock_send
    ):
        """
        If EmailMessage.send() raises an exception, the contact view should:
        - stay on / return to the contact page
        - display an error message to the user
        """
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Test subject",
            "message": "Hello!",
        }

        response = self.client.post(reverse("contact"), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/contact.html")
        storage = get_messages(response.wsgi_request)
        messages = [str(m) for m in storage]

        self.assertTrue(
            any(
                "An error occurred while sending your message" in m
                for m in messages
            ),
            f"Expected error message not found. Messages were: {messages}"
        )
        mock_send.assert_called_once()
