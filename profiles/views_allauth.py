from allauth.account.views import EmailView
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class RemoveEmail(EmailView):
    """
    Ensure at least one email always remains on the account.
    Prevent removing the primary email unless another is made primary first.
    """
    def post(self, request, *args, **kwargs):
        if "action_remove" in request.POST:
            emails = request.user.emailaddress_set.all()

            if emails.count() <= 1:
                messages.error(
                    request,
                    _("You must keep at least one email address on your account.")
                )
                return redirect("account_email")

            selected_email = request.POST.get("email")
            if not selected_email:
                messages.error(
                    request,
                    _("Please select an email address to remove.")
                )
                return redirect("account_email")

            selected_obj = emails.filter(email=selected_email).first()
            if selected_obj and selected_obj.primary:
                messages.error(
                    request,
                    _("You cannot remove your primary email. Make another email primary first.")
                )
                return redirect("account_email")

        return super().post(request, *args, **kwargs)
