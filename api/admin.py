from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("EXTRA"), {
            "fields": ("phone", "status")
        }),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Tablet)
admin.site.register(In)
admin.site.register(Order)
admin.site.register(Order_Item)