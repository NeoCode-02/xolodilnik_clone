from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "phone_number", "first_name", "last_name", "is_active", "is_confirmed", "is_staff", "is_superuser")
    search_fields = ("email", "phone_number", "first_name", "last_name")
    list_filter = ("is_active", "is_confirmed", "is_staff", "is_superuser")
    search_fields = ("email", "phone_number", "first_name", "last_name")
    ordering = ("id",)
    fieldsets = (
        (None, {"fields": ("email", "phone_number", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "avatar")}),
        ("Permissions", {"fields": ("is_active", "is_confirmed", "is_staff", "is_superuser")}),
    )