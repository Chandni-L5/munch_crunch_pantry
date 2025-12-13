from django.conf import settings

from decimal import Decimal, InvalidOperation
from typing import Optional, Dict, Any


def get_discount_amount(request)
    """Retrieve discount amount from session if available."""
    discount = request.session.get('discount_amount') or {}
    discount_code = discount.get('code')
    if not discount_code:
        return None
    
    available_codes = getattr(settings, 'DISCOUNT_CODES', {})
    percentage = available_codes.get(discount_code.upper())
    if percentage is None:
        request.session.pop('discount_amount', None)
        return None
    
    try:
        percentage_decimal = Decimal(str(percentage))
    except (InvalidOperation, ValueError):
        request.session.pop('discount_amount', None)
        return None
    
    if percentage_decimal <= 0:
        request.session.pop('discount_amount', None)
        return None
    
    return {'code':discount_code.upper(), 'percentage': percentage_decimal}
