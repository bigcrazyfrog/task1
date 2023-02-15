from django.urls import path
from .transport.rest.handlers import UserInfo

urlpatterns = [
    path('userinfo/<int:telegram_id>/', UserInfo.get)
]
