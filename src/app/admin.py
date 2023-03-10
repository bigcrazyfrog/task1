from django.contrib import admin

from app.internal.admin.admin_user import AdminUserAdmin
from .models import UserProfile

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram_id', 'phone_number')