from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from api.models.user_profile import UserProfile
from api.models.relationship import Relationship
from api.models.post import Post
from api.models.post_tag import PostTag
from api.models.post_like import PostLike
from api.models.post_comment import PostComment

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
        (("Important dates"), {"fields": ("last_login",)})
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
admin.site.register(UserProfile)
admin.site.register(Relationship)
admin.site.register(Post)
admin.site.register(PostTag)
admin.site.register(PostLike)
admin.site.register(PostComment)
