from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractBaseUser, PermissionsMixin):
    """
    An class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(_('full name'), max_length=100, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    created_at = models.DateTimeField(_("date joined"), default=timezone.now)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

