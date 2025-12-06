from django import forms
from django_countries.widgets import CountrySelectWidget
from .models import Order


class OrderForm(forms.ModelForm):
    address_search = forms.CharField(
        required=False,
        label="Address Search",
        widget=forms.TextInput(attrs={"placeholder": "Start typing your address...", "class": "form-control", }),
    )

    class Meta:
        model = Order
        fields = [
            "full_name",
            "email",
            "phone_number",
            "address_search",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={"placeholder": "Full name*", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "id": "id_email",
                    "placeholder": "Email address*",
                    "class": "form-control",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "id": "id_phone_number",
                    "placeholder": "Phone number*",
                    "class": "form-control",
                }
            ),
            "street_address1": forms.TextInput(
                attrs={"placeholder": "Street address 1*", "class": "form-control"}
            ),
            "street_address2": forms.TextInput(
                attrs={
                    "placeholder": "Apartment, flat, suite (optional)",
                    "class": "form-control",
                }
            ),
            "town_or_city": forms.TextInput(
                attrs={"placeholder": "Town or city*", "class": "form-control"}
            ),
            "postcode": forms.TextInput(
                attrs={"placeholder": "Postcode*", "class": "form-control"}
            ),
            "country": CountrySelectWidget(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["address_search"].required = False
        self.fields["street_address2"].required = False

        for name, field in self.fields.items():
            field.widget.attrs.setdefault("class", "form-control")
            field.label = False
