import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from .models import NewsletterSubscriber


@require_POST
@csrf_protect
def subscribe(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid request."}, status=400)

    email = (payload.get("email") or "").strip().lower()

    if not email:
        return JsonResponse({"error": "Email is required."}, status=400)

    obj, created = NewsletterSubscriber.objects.get_or_create(email=email)
    if created:
        return JsonResponse(
            {"message": "🎉 Thanks — you’re subscribed!"}, status=201
        )

    return JsonResponse(
        {"message": "You’re already subscribed. ✅"}, status=200
    )
