from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.domain.entities.post_like import PostLike as PostLikeEntity
from .user_profile import UserProfile
from .post import Post


class PostLike(models.Model):
    profile = models.ForeignKey(UserProfile, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now, editable=False)

    def to_entity(self) -> PostLikeEntity:
        return PostLikeEntity(
            id=self.pk,
            profile_id=self.profile.pk,
            post_id=self.post.id,
            created_at=self.created_at
        )

    @staticmethod
    def from_entity(post_like: PostLikeEntity) -> "PostLike":
        return PostLike(
            profile_id=post_like.profile_id,
            post_id=post_like.post_id,
            created_at=post_like.created_at
        )

    class Meta:
        verbose_name = "post tag"
        verbose_name_plural = "post tags"