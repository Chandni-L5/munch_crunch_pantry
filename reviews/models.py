from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db.models import Avg, Count


class Review(models.Model):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
    )
    comment = models.TextField(max_length=500, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'user'],
                name='unique_review_per_user_per_product'
            )
        ]

    def __str__(self):
        star_icon = '<i class="fa-solid fa-star"></i>'
        return (
            f'{self.product} | {self.user} - '
            f'Rating: {self.rating}{star_icon}'
        )

    @staticmethod
    def approved_for_product(product_id):
        return Review.objects.filter(product=product_id, is_approved=True)
