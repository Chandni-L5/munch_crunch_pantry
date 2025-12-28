from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from products.models import Product
from .models import Review


User = get_user_model()


class ReviewModelTests(TestCase):
    """
    Test suite for the Review model.
    """
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@test.com",
            password="password123",
        )
        self.user2 = User.objects.create_user(
            username="user2",
            email="user2@test.com",
            password="password123",
        )

        self.product = Product.objects.create(
            name="Test Product",
            description="A simple description",
        )

    def test_defaults_are_set_correctly(self):
        """
        Test that default values are set correctly upon creation.
        """
        review = Review.objects.create(
            product=self.product,
            user=self.user1,
            rating=4,
            comment="Nice!",
        )
        self.assertFalse(review.is_approved)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_str_returns_expected_format(self):
        """
        Test that __str__ includes product name, username and rating.
        """
        review = Review.objects.create(
            product=self.product,
            user=self.user1,
            rating=5,
        )
        expected = (
            f"{self.product} | {self.user1} - Rating: 5"
            "<i class=\"fa-solid fa-star\"></i>"
        )
        self.assertEqual(str(review), expected)

    def test_unique_constraint_one_review_per_user_per_product(self):
        """
        Test that a user cannot create more than one review per product.
        """
        Review.objects.create(
            product=self.product,
            user=self.user1,
            rating=4,
        )

        with self.assertRaises(IntegrityError):
            Review.objects.create(
                product=self.product,
                user=self.user1,
                rating=3,
            )

    def test_approved_for_product_returns_only_approved_reviews(self):
        """
        Test that approved_for_product returns only approved reviews
        for the given product.
        """
        approved = Review.objects.create(
            product=self.product,
            user=self.user1,
            rating=5,
            is_approved=True,
        )
        Review.objects.create(
            product=self.product,
            user=self.user2,
            rating=2,
            is_approved=False,
        )

        qs = Review.approved_for_product(self.product.id)
        self.assertIn(approved, qs)
        self.assertEqual(qs.count(), 1)
        self.assertTrue(all(r.is_approved for r in qs))
