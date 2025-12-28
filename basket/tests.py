from decimal import Decimal
from django.test import TestCase, RequestFactory, override_settings
from .utils import get_discount_amount


class GetDiscountAmountTests(TestCase):
    """
    Tests for get_discount_amount utility function.
    """

    def setUp(self):
        self.factory = RequestFactory()

    def _get_request_with_session(self):
        """
        Helper to attach a session to a RequestFactory request.
        """
        request = self.factory.get("/")
        request.session = {}
        return request

    def test_returns_invalid_when_no_discount_in_session(self):
        """
        No discount in session should return invalid result.
        """
        request = self._get_request_with_session()

        result = get_discount_amount(request)

        self.assertFalse(result["valid"])
        self.assertIsNone(result["code"])
        self.assertEqual(result["percentage"], Decimal("0"))

    @override_settings(DISCOUNT_CODES={"SAVE10": 10})
    def test_valid_discount_code_returns_percentage(self):
        """
        Valid discount code in session returns correct percentage.
        """
        request = self._get_request_with_session()
        request.session["discount_amount"] = {"code": "save10"}

        result = get_discount_amount(request)

        self.assertTrue(result["valid"])
        self.assertEqual(result["code"], "SAVE10")
        self.assertEqual(result["percentage"], Decimal("10"))

    @override_settings(DISCOUNT_CODES={"SAVE10": 10})
    def test_invalid_discount_code_is_removed_from_session(self):
        """
        Invalid discount code should be removed from session
        and return invalid result.
        """
        request = self._get_request_with_session()
        request.session["discount_amount"] = {"code": "BADCODE"}

        result = get_discount_amount(request)

        self.assertFalse(result["valid"])
        self.assertIsNone(result["code"])
        self.assertEqual(result["percentage"], Decimal("0"))
        self.assertNotIn("discount_amount", request.session)

    @override_settings(DISCOUNT_CODES={"SAVE0": 0})
    def test_zero_or_negative_percentage_is_rejected(self):
        """
        Discount codes with zero or negative values are rejected.
        """
        request = self._get_request_with_session()
        request.session["discount_amount"] = {"code": "SAVE0"}

        result = get_discount_amount(request)

        self.assertFalse(result["valid"])
        self.assertIsNone(result["code"])
        self.assertEqual(result["percentage"], Decimal("0"))
        self.assertNotIn("discount_amount", request.session)
