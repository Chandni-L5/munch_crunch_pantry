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


class CategoryModelTests(TestCase):
    """ Test to check Slug is generated correctly from Name """
    def test_category_str_returns_name(self):
        category = Category.objects.create(name="Nuts")
        self.assertEqual(str(category), "Nuts")

    def test_slug_is_auto_generated_from_name(self):
        category = Category.objects.create(name="Nuts")
        self.assertEqual(category.slug, "nuts")


class ProductModelTests(TestCase):
    """ Test to check Product model functionality
    - product name is returned correctly
    - SKU is auto-generated if not provided
    - from_price, lowest_price, highest_price methods work correctly
    - handle case with no quantities
    """
    def setUp(self):
        self.category = Category.objects.create(name="Nuts")
        self.product = Product.objects.create(
            category=self.category,
            name="Almonds",
            description="Tasty almonds",
        )

    def test_product_str_returns_name(self):
        self.assertEqual(str(self.product), "Almonds")

    def test_sku_auto_generated_if_not_provided(self):
        self.assertIsNotNone(self.product.sku)
        self.assertEqual(len(self.product.sku), 8)
        self.assertTrue(self.product.sku.isupper())

    def test_from_price_and_lowest_highest_price(self):
        q_250g = Quantity.objects.create(name="250g")
        q_500g = Quantity.objects.create(name="500g")

        ProductQuantity.objects.create(
            product=self.product,
            quantity=q_250g,
            price=Decimal("3.50"),
            stock=10,
        )
        ProductQuantity.objects.create(
            product=self.product,
            quantity=q_500g,
            price=Decimal("5.99"),
            stock=5,
        )

        self.assertEqual(self.product.from_price(), Decimal("3.50"))
        self.assertEqual(self.product.lowest_price(), Decimal("3.50"))
        self.assertEqual(self.product.highest_price(), Decimal("5.99"))

    def test_lowest_price_none_if_no_quantities(self):
        other_product = Product.objects.create(
            category=self.category,
            name="Cashews",
            description="Yum",
        )
        self.assertIsNone(other_product.lowest_price())
        self.assertIsNone(other_product.highest_price())


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
