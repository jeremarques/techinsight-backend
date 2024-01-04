from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from api.domain.entities.post_tag import PostTag as PostTagEntity

class PostTag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now)

    def to_entity(self) -> PostTagEntity:
        return PostTagEntity(
            name=self.name,
            slug=self.slug,
            created_at=self.created_at
        )

    @staticmethod
    def from_entity(post_tag: PostTagEntity) -> "PostTag":
        return PostTag(
            name=post_tag.name,
            slug=slugify(post_tag.slug),
            created_at=post_tag.created_at
        )

    class Meta:
        verbose_name = "post tag"
        verbose_name_plural = "post tags"