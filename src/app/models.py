from app.internal.models.admin_user import AdminUser

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    telegram_id = models.PositiveIntegerField(
        verbose_name='telegram ID',
        unique=True,
        null=False,
    )
    phone_number = PhoneNumberField(
        verbose_name='phone number',
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.telegram_id}"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'