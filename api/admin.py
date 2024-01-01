from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'is_superuser', 'is_staff', 'created_at']
    list_filter = ['is_superuser']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email')}),
        (
            'Permissions', 
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
        (("Important dates"), {"fields": ("last_login", "created_at")})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ['username']
    ordering = ['created_at']
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

