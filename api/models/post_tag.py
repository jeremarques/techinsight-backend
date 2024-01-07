from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.domain.entities.post_tag import PostTag as PostTagEntity

class PostTag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now, editable=False)
    updated_at = models.DateTimeField("updated at", null=True, editable=False)

    def to_entity(self) -> PostTagEntity:
        return PostTagEntity(
            id=self.pk,
            name=self.name,
            slug=self.slug,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    @staticmethod
    def from_entity(post_tag: PostTagEntity) -> "PostTag":
        return PostTag(
            name=post_tag.name,
            slug=post_tag.slug,
            created_at=post_tag.created_at,
            updated_at=post_tag.updated_at
        )

    class Meta:
        verbose_name = "post tag"
        verbose_name_plural = "post tags"