import json
from unittest.mock import patch

from django.http import HttpResponse
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from checkout.forms import OrderForm
from checkout.models import Order
from checkout.webhook_handler import StripeWH_Handler


class CreatePaymentIntentTests(TestCase):
    """
    Test check for Stripe payment intent creation with empty basket.
    """

    @patch("checkout.views.stripe.PaymentIntent.create")
    def test_create_payment_intent_returns_error_when_basket_empty(
        self, mock_stripe
    ):
        client = Client()

        response = client.post(
            reverse("create_payment_intent"),
            data="{}",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        mock_stripe.assert_not_called()


class CacheCheckoutDataTests(TestCase):
    """
    Test caching checkout data to Stripe payment intent metadata."""

    @patch("checkout.views.stripe.PaymentIntent.modify")
    def test_cache_checkout_data_updates_metadata(self, mock_modify):
        client = Client()

        response = client.post(
            reverse("cache_checkout_data"),
            data=json.dumps(
                {
                    "client_secret": "pi_123_secret_abcd",
                    "save_info": True,
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        mock_modify.assert_called_once()


class WebhookViewTests(TestCase):
    """
    Check webhook view handles events correctly.
    - Bad JSON returns 400
    - Valid event dispatches to handler
    """

    def setUp(self):
        self.client = Client()

    def test_webhook_bad_json_returns_400(self):
        response = self.client.post(
            reverse("webhook"),
            data="not-json",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    @patch("checkout.webhooks.stripe.Webhook.construct_event")
    @patch("checkout.webhooks.StripeWH_Handler")
    def test_webhook_dispatches_to_handler(
        self, mock_handler_cls, mock_construct_event
    ):
        payload = {
            "type": "payment_intent.succeeded",
            "data": {"object": {}},
        }

        mock_construct_event.return_value = payload
        mock_handler_instance = mock_handler_cls.return_value
        mock_handler_instance.handle_payment_intent_succeeded.return_value = (
            HttpResponse(status=200)
        )

        response = self.client.post(
            reverse("webhook"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="fake_signature",
        )

        self.assertEqual(response.status_code, 200)
        mock_construct_event.assert_called_once()
        mock_handler_cls.assert_called_once()
        mock_handler_instance.handle_payment_intent_succeeded\
            .assert_called_once_with(payload)


class WebhookHandlerTests(TestCase):
    """
    Tests Stripe webhook handler methods to check 
    it won't crash or create duplicate orders.
    """

    def setUp(self):
        self.factory = RequestFactory()

    def test_handle_payment_intent_succeeded_marks_order_as_paid(self):
        order = Order.objects.create(
            full_name="Test User",
            email="test@example.com",
            phone_number="1234567890",
            country="GB",
            postcode="AB1 2CD",
            town_or_city="Testtown",
            street_address1="123 Test Street",
            street_address2="",
            original_basket="{}",
            stripe_pid="pi_test_123",
            is_paid=False,
            confirmation_email_sent=False,
        )

        event = {
            "type": "payment_intent.succeeded",
            "data": {"object": {"id": "pi_test_123"}},
        }

        request = self.factory.post("/checkout/webhook/")
        handler = StripeWH_Handler(request=request)
        response = handler.handle_payment_intent_succeeded(event)

        self.assertEqual(response.status_code, 200)

        order.refresh_from_db()
        self.assertTrue(order.is_paid)

    def test_handle_payment_intent_succeeded_returns_200_when_no_order_found(
        self
    ):
        event = {
            "type": "payment_intent.succeeded",
            "data": {"object": {"id": "pi_missing"}},
        }

        request = self.factory.post("/checkout/webhook/")
        handler = StripeWH_Handler(request=request)
        response = handler.handle_payment_intent_succeeded(event)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), 0)


class OrderFormTests(TestCase):
    """
    Basic test to ensure OrderForm requires full_name.
    """

    def test_form_requires_full_name(self):
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("full_name", form.errors)
