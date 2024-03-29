from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    list_display = ["username", "is_active", "is_superuser", "date_joined"]
    search_fields = ["username"]
