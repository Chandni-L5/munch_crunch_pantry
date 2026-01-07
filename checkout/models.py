import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from decimal import Decimal

from profiles.models import UserProfile
from core.validators import validate_phone_digits


class Order(models.Model):
    order_number = models.CharField(
        max_length=32, unique=True, null=False, editable=False
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(
        max_length=20, null=False, blank=False,
        validators=[validate_phone_digits]
    )
    country = CountryField(default='GB')
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    discount_code = models.CharField(max_length=50, null=True, blank=True)
    discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=Decimal("0.00")
    )
    original_basket = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        lineitem_total = (
            self.lineitems.aggregate(
                Sum("lineitem_total")
            )["lineitem_total__sum"] or Decimal("0.00")
        )

        self.order_total = lineitem_total

        discounted_total = self.order_total - self.discount_amount
        if discounted_total < 0:
            discounted_total = Decimal("0.00")

        free_threshold = Decimal(str(settings.FREE_DELIVERY_THRESHOLD))
        standard_delivery = Decimal(str(settings.STANDARD_DELIVERY))

        if discounted_total == 0:
            self.delivery_cost = Decimal("0.00")
        elif discounted_total < free_threshold:
            self.delivery_cost = standard_delivery
        else:
            self.delivery_cost = Decimal("0.00")

        self.grand_total = discounted_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """Set the order number if it hasn't been set already."""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product_quantity = models.ForeignKey(
        "products.ProductQuantity",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        """
        Set the lineitem total from the ProductQuantity price
        """
        self.lineitem_total = self.product_quantity.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Use the Product's SKU (or name) instead of non-existent
        ProductQuantity.sku.
        """
        product = self.product_quantity.product
        return (
            f"SKU {product.sku} "
            f"({product.name} - {self.product_quantity.quantity.name}) "
            f"on order {self.order.order_number}"
        )


class DiscountSingleUse(models.Model):
    """Model to track single-use discount codes per user
    - linked the the email address attached to the order
    """
    code = models.CharField(max_length=50)
    email = models.EmailField()
    used_at = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=32, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'email'],
                name='unique_discount_per_email'
            )
        ]

    def __str__(self):
        return f"Discount code {self.code} used by {self.email}"
