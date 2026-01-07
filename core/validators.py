from django.core.exceptions import ValidationError


def validate_phone_digits(value):
    """
    Validates that a phone number contains 7–15 digits.
    Allows spaces, brackets, +, etc.
    """
    if not value:
        return

    digits = "".join(char for char in value if char.isdigit())

    if len(digits) < 7 or len(digits) > 15:
        raise ValidationError(
            "Enter a valid phone number (7–15 digits)."
        )
