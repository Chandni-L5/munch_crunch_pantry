from decimal import Decimal

from django.test import TestCase
from django.db import IntegrityError

from products.models import (
    Category,
    Product,
    Quantity,
    ProductQuantity,
    NutritionMetric,
    NutritionLabel,
)


class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Nuts", slug="nuts")

        self.product = Product.objects.create(
            category=self.category,
            name="Almonds",
            description="Tasty almonds",
        )

        self.q250 = Quantity.objects.create(name="250g")
        self.q500 = Quantity.objects.create(name="500g")
        self.q1kg = Quantity.objects.create(name="1kg")

        ProductQuantity.objects.create(
            product=self.product, quantity=self.q250,
            price=Decimal("3.50"), stock=10
        )
        ProductQuantity.objects.create(
            product=self.product, quantity=self.q500,
            price=Decimal("5.99"), stock=5
        )
        ProductQuantity.objects.create(
            product=self.product, quantity=self.q1kg,
            price=Decimal("9.99"), stock=2
        )

    def test_from_price_and_lowest_highest_price(self):
        """
        from_price() returns the lowest ProductQuantity price (or None).
        """
        self.assertEqual(self.product.from_price(), Decimal("3.50"))
        self.assertEqual(self.product.lowest_price, Decimal("3.50"))
        self.assertEqual(self.product.highest_price(), Decimal("9.99"))

    def test_lowest_and_highest_price_none_if_no_quantities(self):
        """
        If a product has no related ProductQuantity rows:
        - lowest_price property should be None
        - highest_price() method should return None
        - from_price() should return None
        """
        other_product = Product.objects.create(
            category=self.category,
            name="Cashews",
            description="Tasty cashews",
        )

        self.assertIsNone(other_product.from_price())
        self.assertIsNone(other_product.lowest_price)
        self.assertIsNone(other_product.highest_price())


class CategoryModelTests(TestCase):
    """ Test to check Slug is generated correctly from Name """
    def test_category_str_returns_name(self):
        category = Category.objects.create(name="Nuts")
        self.assertEqual(str(category), "Nuts")

    def test_slug_is_auto_generated_from_name(self):
        category = Category.objects.create(name="Nuts")
        self.assertEqual(category.slug, "nuts")


class QuantityModelTests(TestCase):
    """ Test to check string representation returns name """
    def test_quantity_str_returns_name(self):
        q = Quantity.objects.create(name="1kg")
        self.assertEqual(str(q), "1kg")


class ProductQuantityModelTests(TestCase):
    """ Test to check ProductQuantity model functionality
    - string representation combines product name and quantity name
    - unique_together constraint on (product, quantity)
    - integrity error raised on duplicate entries
    """
    def setUp(self):
        self.category = Category.objects.create(name="Seeds")
        self.product = Product.objects.create(
            category=self.category,
            name="Chia Seeds",
            description="High in omega-3",
        )
        self.quantity = Quantity.objects.create(name="500g")

    def test_product_quantity_str(self):
        pq = ProductQuantity.objects.create(
            product=self.product,
            quantity=self.quantity,
            price=Decimal("4.50"),
            stock=20,
        )
        self.assertEqual(str(pq), "Chia Seeds - 500g")

    def test_product_quantity_unique_together(self):
        ProductQuantity.objects.create(
            product=self.product,
            quantity=self.quantity,
            price=Decimal("4.50"),
            stock=20,
        )
        with self.assertRaises(IntegrityError):
            ProductQuantity.objects.create(
                product=self.product,
                quantity=self.quantity,
                price=Decimal("4.99"),
                stock=5,
            )


class NutritionModelsTests(TestCase):
    """ Test to check NutritionMetric and NutritionLabel models
    - string representations are displayed correctly in admin
    - integrity error raised on duplicate NutritionLabel entries
    """
    def setUp(self):
        self.category = Category.objects.create(name="Dried Fruit")
        self.product = Product.objects.create(
            category=self.category,
            name="Dried Apricots",
            description="Chewy and tangy",
        )
        self.metric_energy = NutritionMetric.objects.create(
            name="Energy",
            unit="kcal",
        )

    def test_nutrition_metric_str(self):
        self.assertEqual(str(self.metric_energy), "Energy (kcal)")

    def test_nutrition_label_str(self):
        label = NutritionLabel.objects.create(
            product=self.product,
            metric=self.metric_energy,
            amount_per_100g=Decimal("240.00"),
        )
        self.assertEqual(str(label), "Dried Apricots - Energy")

    def test_nutrition_label_unique_together(self):
        NutritionLabel.objects.create(
            product=self.product,
            metric=self.metric_energy,
            amount_per_100g=Decimal("240.00"),
        )
        with self.assertRaises(IntegrityError):
            NutritionLabel.objects.create(
                product=self.product,
                metric=self.metric_energy,
                amount_per_100g=Decimal("250.00"),
            )
