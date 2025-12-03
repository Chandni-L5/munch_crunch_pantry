from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Full name"}),
            "email": forms.EmailInput(
                attrs={"id": "id_email", "placeholder": "Email address"}
            ),
            "phone_number": forms.TextInput(
                attrs={"id": "id_phone_number", "placeholder": "Phone number"}
            ),
            "street_address1": forms.TextInput(attrs={"placeholder": "Street address"}),
            "street_address2": forms.TextInput(attrs={"placeholder": "Street address"}),
            "town_or_city": forms.TextInput(attrs={"placeholder": "Town or city"}),
            "postcode": forms.TextInput(attrs={"placeholder": "Postcode"}),
            "country": forms.TextInput(attrs={"placeholder": "Country"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != "street_address2":
                field.required = True


def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes,
    remove auto-generated labels
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        "full_name": "Full Name",
        "email": "Email Address",
        "phone_number": "Phone Number",
        "street_address1": "Street Address 1",
        "street_address2": "Street Address 2",
        "town_or_city": "Town or City",
        "postcode": "Postal Code",
        "country": "Country",
    }

    self.fields["full_name"].widget.attrs["autofocus"] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f"{placeholders[field]} *"
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs["placeholder"] = placeholder
        self.fields[field].widget.attrs["class"] = "stripe-style-input"
        self.fields[field].label = False
