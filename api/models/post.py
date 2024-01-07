import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .user_profile import UserProfile
from .post_tag import PostTag
from api.domain.entities.post import Post as PostEntity


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    public_id = models.CharField('ID used for public posts URL', max_length=14, unique=True)
    profile = models.ForeignKey(UserProfile, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    content = models.TextField()
    tag = models.ForeignKey(PostTag, related_name='posts', on_delete=models.PROTECT)
    likes_counter = models.PositiveIntegerField('likes counter', default=0)
    created_at = models.DateTimeField(_('date joined'), default=timezone.now, editable=False)
    updated_at = models.DateTimeField('updated at', null=True, editable=False)

    def to_entity(self) -> PostEntity:
        return PostEntity(
            id=self.id,
            public_id=self.public_id,
            profile=self.profile.to_entity(),
            title=self.title,
            slug=self.slug,
            content=self.content,
            tag=self.tag.to_entity(),
            likes=self.likes_counter,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    @staticmethod
    def from_entity(post_entity: PostEntity) -> "Post":
        return Post(
            public_id=post_entity.public_id,
            profile_id=post_entity.profile.id,
            title=post_entity.title,
            slug=post_entity.slug,
            content=post_entity.content,
            tag_id=post_entity.tag.id,
            likes_counter=post_entity.likes,
            created_at=post_entity.created_at,
            updated_at=post_entity.updated_at
        )

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
