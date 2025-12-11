from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ContactMessage, UserProfile
from .forms import UserProfileForm, UserUpdateForm

from checkout.models import Order


@login_required
def profile(request):
    """ A view to return the user's profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    contact_messages = ContactMessage.objects.filter(user_profile=profile).order_by('-created_at')

    if request.method == 'POST':
        delivery_form = UserProfileForm(request.POST, instance=profile)
        profile_form = UserUpdateForm(request.POST, instance=request.user)
        if delivery_form.is_valid() and profile_form.is_valid():
            delivery_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please check the form.')
    else:
        delivery_form = UserProfileForm(instance=profile)
        profile_form = UserUpdateForm(instance=request.user)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'delivery_form': delivery_form,
        'profile_form': profile_form,
        'orders': orders,
        'profile': profile,
        'on_profile_page': True,
        'contact_messages': contact_messages,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user_profile=request.user.userprofile,
    )

    from_email = request.GET.get("from_email") == "1"

    if not from_email:
        messages.info(
            request,
            (
                f"This is a past confirmation for order number {order_number}. "
                "A confirmation email was sent on the order date."
            )
        )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
        "from_email": from_email,
    }

    return render(request, template, context)
