from django.http import JsonResponse

from app.models import UserProfile


def user_info(request, telegram_id):
    info = dict(
        exist=False,
        telegram_id=None,
        phone_number=None,
    )

    try:
        user = UserProfile.objects.get(telegram_id=telegram_id)

        info['exist'] = True
        info['telegram_id'] = telegram_id
        info['phone_number'] = user.telegram_id

    except Exception:
        pass

    return JsonResponse(info)
