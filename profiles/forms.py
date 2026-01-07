from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from allauth.account.forms import SignupForm

from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    """
    Form to update user information
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
        }

        for field_name in self.fields:
            field = self.fields[field_name]
            field.required = True
            field.widget.attrs['class'] = 'profile-form-input'
            field.widget.attrs['placeholder'] = (
                placeholders[field_name]
            )
            field.label = False

        self.fields['first_name'].error_messages['required'] = (
            "Please enter your first name."
        )
        self.fields['last_name'].error_messages['required'] = (
            "Please enter your last name."
        )
        self.fields['username'].error_messages['required'] = (
            "Please choose a username."
        )


class UserProfileForm(forms.ModelForm):
    """
    Form to manage user delivery information
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }

        for field_name in self.fields:
            self.fields[field_name].required = True

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field_name in self.fields:
            if field_name != 'default_country':
                self.fields[field_name].widget.attrs['placeholder'] = (
                    placeholders[field_name]
                )
            self.fields[field_name].widget.attrs['class'] = (
                'profile-form-input'
            )
            self.fields[field_name].label = False
            self.fields['default_street_address2'].required = False


User = get_user_model()


class CustomSignupForm(SignupForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError(
                "This username is already taken. Please choose another."
            )
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(
                "An account with this email already exists."
                " Please sign in or reset your password."
            )
        return email
