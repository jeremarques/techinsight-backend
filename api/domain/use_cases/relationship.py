from api.domain.entities.relationship import Relationship
from api.infrastructure.adapters.repositories.relationship import RelationshipRepository
from api.infrastructure.adapters.repositories.user import UserRepository
from api.errors import NotFoundException, AlreadyExistsException


class FollowUserUseCase:
    def __init__(self, relationship_repository: RelationshipRepository, user_repository: UserRepository) -> None:
        self.relationship_repository = relationship_repository
        self.user_repository = user_repository

    def execute(self, follower_id: int, followed_id: int) -> Relationship:

        if not self.user_repository.exists(id=followed_id):
            raise NotFoundException('O usuário que você deseja seguir não foi encontrado.')
        
        if self.relationship_repository.is_following(follower_id, followed_id):
            raise AlreadyExistsException('Você já segue esse usuário.')
        
        relationship_entity = Relationship(follower_id, followed_id)

        try:
            created_relationship_entity = self.relationship_repository.save(relationship_entity)

        except Exception:
            raise Exception('Ocorreu um erro ao seguir o usuário.')

        return created_relationship_entity
    

class UnfollowUserUseCase:
    def __init__(self, relationship_repository: RelationshipRepository, user_repository: UserRepository) -> None:
        self.relationship_repository = relationship_repository
        self.user_repository = user_repository

    def execute(self, follower_id: int, followed_id: int) -> None:
        
        if not self.relationship_repository.is_following(follower_id, followed_id):
            raise NotFoundException('Você não segue esse usuário')

        try:
            self.relationship_repository.delete(follower_id, followed_id)

        except Exception:
            raise Exception('Ocorreu um erro ao parar de seguir o usuário.')

        return None