from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.domain.entities.post_comment import PostComment as PostCommentEntity
from .user_profile import UserProfile
from .post import Post


class PostComment(models.Model):
    profile = models.ForeignKey(UserProfile, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(_('date joined'), default=timezone.now, editable=False)
    updated_at = models.DateTimeField('updated at', null=True, editable=False)

    def to_entity(self) -> PostCommentEntity:
        return PostCommentEntity(
            id=self.pk,
            profile=self.profile.to_entity(),
            post_id=self.post.id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    @staticmethod
    def from_entity(post_comment: PostCommentEntity) -> "PostComment":
        return PostComment(
            profile_id=post_comment.profile.id,
            post_id=post_comment.post_id,
            created_at=post_comment.created_at,
            updated_at=post_comment.updated_at
        )

    class Meta:
        verbose_name = "post comment"
        verbose_name_plural = "post comments"