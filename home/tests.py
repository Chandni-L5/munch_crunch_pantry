from django.test import TestCase
from django.urls import reverse


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
