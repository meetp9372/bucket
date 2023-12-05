from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from user import models


@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("username", "first_name", "last_name", "is_active", "is_staff")

    # Fieldsets for add and change forms
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",

                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("Important dates", {"fields": ("date_joined",)}),
    )

    # Adding new fields if present in your custom user model
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
