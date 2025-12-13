from django.conf import settings

from decimal import Decimal, InvalidOperation


def get_discount_amount(request):
    """
    Retrieve discount amount from session if available.
    Validate against available discount codes in settings.
    """
    discount = request.session.get('discount_amount') or {}
    discount_code = (discount.get('code') or "").strip().upper()

    if not discount_code:
        return {'valid': False, 'code': None, 'percentage': Decimal("0")}

    available_codes = getattr(settings, 'DISCOUNT_CODES', {})
    percentage = available_codes.get(discount_code)

    if percentage is None:
        request.session.pop('discount_amount', None)
        return {'valid': False, 'code': None, 'percentage': Decimal("0")}

    try:
        percentage_decimal = Decimal(str(percentage))
    except (InvalidOperation, ValueError):
        request.session.pop('discount_amount', None)
        return {'valid': False, 'code': None, 'percentage': Decimal("0")}

    if percentage_decimal <= 0:
        request.session.pop('discount_amount', None)
        return {'valid': False, 'code': None, 'percentage': Decimal("0")}

    return {
        'valid': True,
        'code': discount_code.upper(),
        'percentage': percentage_decimal
    }
