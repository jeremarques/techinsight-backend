from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.domain.entities.user_profile import UserProfile as UserProfileEntity
from api.models.user import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    profile_photo = models.URLField(blank=True)
    website = models.URLField(blank=True)
    name = models.CharField(max_length=60)
    bio = models.CharField(max_length=200, blank=True)
    about = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now, editable=False)
    updated_at = models.DateTimeField("updated at", null=True, editable=False)

    def to_entity(self) -> UserProfileEntity:
        return UserProfileEntity(
            id=self.pk,
            user=self.user.to_entity(),
            profile_photo=self.profile_photo,
            website_url=self.website,
            name=self.name,
            bio=self.bio,
            about=self.about,
            date_of_birth=self.date_of_birth,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    @staticmethod
    def from_entity(profile: UserProfileEntity) -> "UserProfile":
        return UserProfile(
            user_id=profile.user.id,
            profile_photo=profile.profile_photo,
            website=profile.website_url,
            name=profile.name,
            bio=profile.bio,
            about=profile.about,
            date_of_birth=profile.date_of_birth,
            created_at=profile.created_at,
            updated_at=profile.updated_at,
        )

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "users profiles"