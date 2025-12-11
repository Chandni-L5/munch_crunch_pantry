from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your name*"}
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Your email*"}
        )
    )
    subject = forms.CharField(
        max_length=150,
        label="Subject",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Subject - How can we help?"}
        )
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={"class": "form-control",
                   "rows": 5, "placeholder": "Type your message here*"}
        )
    )
    order_number = forms.CharField(
        max_length=50,
        required=False,
        label="Order number (optional)",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Order number (optional)"}
        )
    )
