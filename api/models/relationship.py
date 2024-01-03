from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.domain.entities.relationship import Relationship as RelationshipEntity
from api.models.user import User

class Relationship(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now)

    def to_entity(self) -> RelationshipEntity:
        return RelationshipEntity(
            follower_id=self.follower.id,
            followed_id=self.followed.id,
            created_at=self.created_at
        )

    @staticmethod
    def from_entity(relationship: RelationshipEntity) -> "Relationship":
        return Relationship(
            follower_id=relationship.follower_id,
            followed_id=relationship.followed_id,
            created_at=relationship.created_at
        )

    class Meta:
        verbose_name = "user relationship"
        verbose_name_plural = "users relationships"