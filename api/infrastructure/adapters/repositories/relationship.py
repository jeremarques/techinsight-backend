from api.domain.entities.relationship import Relationship as RelationshipEntity
from api.models.relationship import Relationship

class RelationshipRepository:
    def save(self, relationship: RelationshipEntity) -> RelationshipEntity:
        relationship_model = Relationship.from_entity(relationship)
        relationship_model.save()
        relationship_entity = relationship_model.to_entity()

        return relationship_entity
    
    def delete(self, follower_id: int, followed_id: int) -> None:
        relationship_model = Relationship.objects.filter(follower=follower_id, followed=followed_id)
        relationship_model.delete()

        return None
    
    def is_following(self, follower_id: int, followed_id: int) -> bool:
        relationship = Relationship.objects.filter(follower=follower_id, followed=followed_id)

        if relationship.exists():
            return True
        else:
            return False
        
