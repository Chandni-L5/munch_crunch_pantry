from django.db.models import Avg, Count
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review
from products.models import Product


def recalc_product_rating(product_id):
    qs = Review.objects.filter(product_id=product_id, is_approved=True)
    agg = qs.aggregate(avg=Avg("rating"), count=Count("id"))
    avg = agg["avg"] or 0
    count = agg["count"] or 0

    Product.objects.filter(id=product_id).update(
        rating_avg=avg,
        rating_count=count
    )


@receiver(post_save, sender=Review)
def review_saved(sender, instance, **kwargs):
    recalc_product_rating(instance.product_id)


@receiver(post_delete, sender=Review)
def review_deleted(sender, instance, **kwargs):
    recalc_product_rating(instance.product_id)
