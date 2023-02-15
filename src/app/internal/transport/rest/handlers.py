from django.http import JsonResponse, Http404
from django.views import View

from app.models import UserProfile


class UserInfo(View):
    def get(self, request, telegram_id):
        try:
            user = UserProfile.objects.get(telegram_id=telegram_id)
            return JsonResponse(
                dict(
                    telegram_id=telegram_id,
                    phone_number=user.phone_number
                )
            )
        except Exception:
            return Http404()
