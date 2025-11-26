from django.db import models
from django.db.models import Min, Max
import uuid


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=32, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    sizes = models.ManyToManyField('Quantity', through='ProductQuantity', blank=True, related_name='products')
    image = models.ImageField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    storage_instructions = models.TextField(null=True, blank=True)
    country_of_origin = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    def from_price(self):
        """
        Helper: lowest price across quantities, for admin display.
        """
        pq = self.quantities.order_by('price').first()
        return pq.price if pq else None
    from_price.short_description = "From price"

    def lowest_price(self):
        """ Helper: lowest price across quantities, for product display. """
        agg = self.quantities.aggregate(min_price=Min('price'))
        return agg['min_price']

    def highest_price(self):
        """ Helper: highest price across quantities, for product display. """
        agg = self.quantities.aggregate(max_price=Max('price'))
        return agg['max_price']


class Quantity(models.Model):
    """
    A size option, e.g. 250g, 500g, 1kg.
    """

    class Meta:
        verbose_name_plural = "Quantities"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductQuantity(models.Model):
    """
    Join model linking a product to a specific size (Quantity),
    with its own price and stock.
    """
    product = models.ForeignKey(Product, related_name='quantities', on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'quantity')
        verbose_name_plural = "Product Quantities"

    def __str__(self):
        return f"{self.product.name} - {self.quantity.name}"


class NutritionMetric(models.Model):
    """
    Master list of nutrition metrics, e.g. Energy (kcal), Protein (g).
    """
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20, help_text="E.g. g, mg, kcal")

    def __str__(self):
        return f"{self.name} ({self.unit})"


class NutritionLabel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='nutrition_labels')
    metric = models.ForeignKey(NutritionMetric, on_delete=models.CASCADE)
    amount_per_100g = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('product', 'metric')

    def __str__(self):
        return f"{self.product.name} - {self.metric.name}"
