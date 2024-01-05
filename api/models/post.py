import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .user_profile import UserProfile
from .post_tag import PostTag


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    public_id = models.CharField("ID usado para as urls dos posts", max_lenght=14, unique=True)
    profile = models.ForeignKey(UserProfile, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_lenght=120)
    slug = models.SlugField(max_lenght=120)
    content = models.TextField()
    tag = models.ForeignKey(PostTag, related_name="posts", on_delete=models.PROTECT)
    likes = models.PositiveIntegerField("Quantidade de likes do post", default=0)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now)
