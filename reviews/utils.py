from checkout.models import OrderLineItem


def user_has_purchased_product(user, product) -> bool:
    """
    Return True if the user has bought this product in a completed order.
    """
    if not user.is_authenticated:
        return False

    return OrderLineItem.objects.filter(
        order__user_profile__user=user,
        product_quantity__product=product,
    ).exclude(
        order__stripe_pid=""
    ).exists()
