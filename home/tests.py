from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


# Create your tests here.
class NewsletterBannerTest(TestCase):
    """
     Test to check if the newsletter banner is included in the base template
    """
    def test_newsletter_banner_in_base_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="newsletter-banner"')
        self.assertContains(response, 'id="newsletter-form"')
        self.assertContains(response, 'type="email"')
        self.assertContains(response, 'src="/static/js/newsletter.js"')


class ContactViewTests(TestCase):
    @patch("home.views.EmailMessage.send", side_effect=Exception("boom"))
    def test_contact_shows_error_when_email_fails(self, mock_send):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Test subject",
            "message": "Hello!",
        }
        response = self.client.post(reverse("contact"), data, follow=True)

        self.assertTemplateUsed(response, "home/contact.html")

        messages = list(response.context["messages"])
        self.assertTrue(
            any("Something went wrong" in str(m) for m in messages)
        )
