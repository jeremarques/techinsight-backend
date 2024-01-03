from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.domain.entities.profile import Profile as ProfileEntity
from api.models.user import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.URLField(blank=True)
    website = models.URLField(blank=True)
    name = models.CharField(max_length=60)
    bio = models.CharField(max_length=200, blank=True)
    about = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now)

    def to_entity(self) -> ProfileEntity:
        return ProfileEntity(
            id=self.pk,
            user_id=self.user,
            profile_photo=self.profile_photo,
            website_url=self.website,
            name=self.name,
            bio=self.bio,
            about=self.about,
            date_of_birth=self.date_of_birth,
            created_at=self.created_at
        )

    @staticmethod
    def from_entity(profile: ProfileEntity) -> "Profile":
        return User(
            user=profile.user_id,
            profile_photo=profile.profile_photo,
            website=profile.website_url,
            name=profile.name,
            bio=profile.bio,
            about=profile.about,
            date_of_birth=profile.date_of_birth,
            created_at=profile.created_at
        )

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"