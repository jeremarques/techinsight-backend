from api.domain.entities.relationship import Relationship
from api.infrastructure.adapters.repositories.relationship import RelationshipRepository
from api.infrastructure.adapters.repositories.user import UserRepository
from api.errors import NotFoundException, AlreadyExistsException


class FollowUserUseCase:
    def __init__(self, relationship_repository: RelationshipRepository, user_repository: UserRepository) -> None:
        self.relationship_repository = relationship_repository
        self.user_repository = user_repository

    def execute(self, follower_id: int, followed_id: int) -> Relationship:

        if not self.user_repository.exists_by_id(followed_id):
            raise NotFoundException('O usuário que você deseja seguir não foi encontrado.')
        
        if self.relationship_repository.is_following(follower_id=follower_id, followed_id=followed_id):
            raise AlreadyExistsException('Você já está seguindo este usuário')
        
        relationship_entity = Relationship(
            follower_id=follower_id,
            followed_id=followed_id
        )
        created_relationship_entity = self.relationship_repository.save(relationship_entity)

        return created_relationship_entity
    

class UnfollowUserUseCase:
    def __init__(self, relationship_repository: RelationshipRepository) -> None:
        self.relationship_repository = relationship_repository

    def execute(self, follower_id: int, followed_id: int) -> None:
        
        if not self.relationship_repository.is_following(follower_id=follower_id, followed_id=followed_id):
            raise NotFoundException('Você não segue este usuário')

        self.relationship_repository.delete(follower_id=follower_id, followed_id=followed_id)

        return None