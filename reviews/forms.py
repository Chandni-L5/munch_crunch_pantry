from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]
        widgets = {
            "rating": forms.HiddenInput(),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Write your review...",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get("rating")
        comment = cleaned_data.get("comment", "")

        if not rating:
            self.add_error("rating", "Please select a rating.")

        if not comment.strip():
            self.add_error("comment", "Comment cannot be empty.")

        return cleaned_data
