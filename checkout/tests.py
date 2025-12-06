from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse
from unittest.mock import patch
import json

from checkout.forms import OrderForm
from checkout.webhook_handler import StripeWH_Handler
from checkout.models import Order, OrderLineItem
from products.models import Category, Product, Quantity, ProductQuantity


class CreatePaymentIntentTests(TestCase):
    """
    Tests for create_payment_intent view.
    """

    @patch("checkout.views.stripe.PaymentIntent.create")
    def test_create_payment_intent_returns_error_when_basket_empty(self, mock_stripe):
        client = Client()

        response = client.post(
            reverse("create_payment_intent"),
            data="{}",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        mock_stripe.assert_not_called()


class CacheCheckoutDataTests(TestCase):
    @patch("checkout.views.stripe.PaymentIntent.modify")
    def test_cache_checkout_data_updates_metadata(self, mock_modify):
        client = Client()

        response = client.post(
            reverse("cache_checkout_data"),
            data=json.dumps({
                "client_secret": "pi_123_secret_abcd",
                "save_info": True,
            }),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        mock_modify.assert_called_once()


class WebhookViewTests(TestCase):
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
    def test_webhook_dispatches_to_handler(self, mock_handler_cls, mock_construct_event):
        """
        - construct_event() is called to validate the event
        - StripeWH_Handler is instantiated
        - The correct handler method is called based on event['type']
        """
        payload = {
            "type": "payment_intent.succeeded",
            "data": {"object": {}},
        }

        mock_construct_event.return_value = payload
        mock_handler_instance = mock_handler_cls.return_value
        mock_handler_instance.handle_payment_intent_succeeded.return_value = HttpResponse(status=200)

        response = self.client.post(
            reverse("webhook"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="fake_signature",
        )

        self.assertEqual(response.status_code, 200)
        mock_construct_event.assert_called_once()
        mock_handler_cls.assert_called_once()
        mock_handler_instance.handle_payment_intent_succeeded.assert_called_once_with(payload)


class WebhookHandlerTests(TestCase):
    def _create_product_quantity(self):
        """Helper to create a minimal ProductQuantity row."""
        category = Category.objects.create(name="Nuts")
        product = Product.objects.create(
            category=category,
            name="Almonds",
            description="Test almonds",
        )
        qty = Quantity.objects.create(name="500g")
        pq = ProductQuantity.objects.create(
            product=product,
            quantity=qty,
            price=5.00,
            stock=10,
        )
        return pq

    @patch("checkout.webhook_handler.stripe.Charge.retrieve")
    @patch("checkout.webhook_handler.time.sleep")
    def test_handle_payment_intent_succeeded_creates_order(self, mock_sleep, mock_retrieve_charge):
        """
        Test that a valid payment_intent.succeeded event with basket metadata
        Order and OrderLineItem created.
        """
        pq = self._create_product_quantity()
        basket = {str(pq.id): 2}
        basket_str = json.dumps(basket)

        mock_retrieve_charge.return_value = {
            "id": "ch_test",
            "billing_details": {"email": "test@example.com"},
            "amount": 1000,
        }

        event = {
            "type": "payment_intent.succeeded",
            "data": {
                "object": {
                    "id": "pi_test_123",
                    "metadata": {
                        "basket": basket_str,
                    },
                    "latest_charge": "ch_test",
                    "shipping": {
                        "name": "Test User",
                        "phone": "1234567890",
                        "address": {
                            "line1": "123 Test Street",
                            "line2": "",
                            "city": "test",
                            "postal_code": "AB1 2CD",
                            "country": "GB",
                        },
                    },
                }
            },
        }

        handler = StripeWH_Handler(request=None)
        response = handler.handle_payment_intent_succeeded(event)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderLineItem.objects.count(), 1)

        order = Order.objects.first()
        line_item = OrderLineItem.objects.first()

        self.assertEqual(order.email, "test@example.com")
        self.assertEqual(line_item.product_quantity, pq)
        self.assertEqual(line_item.quantity, 2)

    @patch("checkout.webhook_handler.stripe.Charge.retrieve")
    @patch("checkout.webhook_handler.time.sleep")
    def test_webhook_retries_finding_order(self, mock_sleep, mock_retrieve_charge):
        """
        Test that the handler retries up to 5 times to find an existing order
        before creating a new one.
        """
        pq = self._create_product_quantity()
        basket = {str(pq.id): 1}
        basket_str = json.dumps(basket)

        mock_retrieve_charge.return_value = {
            "id": "ch_test",
            "billing_details": {"email": "retry@example.com"},
            "amount": 500,
        }

        event = {
            "type": "payment_intent.succeeded",
            "data": {
                "object": {
                    "id": "pi_retry",
                    "metadata": {
                        "basket": basket_str,
                    },
                    "latest_charge": "ch_test",
                    "shipping": {
                        "name": "Retry User",
                        "phone": "1234567890",
                        "address": {
                            "line1": "123 Retry Street",
                            "line2": "",
                            "city": "retry test",
                            "postal_code": "AB1 2CD",
                            "country": "GB",
                        },
                    },
                }
            },
        }

        with patch.object(Order.objects, "get", side_effect=Order.DoesNotExist):
            handler = StripeWH_Handler(request=None)
            response = handler.handle_payment_intent_succeeded(event)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_sleep.call_count, 5)
        self.assertEqual(Order.objects.count(), 1)


class OrderFormTests(TestCase):
    """Basic test to ensure OrderForm requires full_name"""
    def test_form_requires_full_name(self):
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("full_name", form.errors)
