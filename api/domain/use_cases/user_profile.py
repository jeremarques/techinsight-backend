from datetime import date
from api.domain.entities.user_profile import UserProfile as UserProfileEntity
from api.domain.entities.user import User as UserEntity
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.repositories.user import UserRepository
from api.domain.dtos.user_profile_dto import UserProfileDTO
from api.domain.dtos.user_dto import UserDTO
from api.errors import NotFoundException


class CreateUserProfileUseCase:
    def __init__(self, user_profile_repository: UserProfileRepository) -> None:
        self.user_profile_repository = user_profile_repository

    def execute(self, user: UserEntity, name: str | None) -> UserProfileEntity:
        user_profile_entity = UserProfileEntity(user=user, name=name)

        try:
            created_user_profile_entity = self.user_profile_repository.save(user_profile_entity)

        except Exception:
            raise Exception('Erro ao criar o perfil do usuário.')

        return created_user_profile_entity


class GetUserProfileUseCase:
    def __init__(self, user_profile_repository: UserProfileRepository, user_repository: UserRepository) -> None:
        self.user_profile_repository = user_profile_repository
        self.user_repository = user_repository

    def execute(self, username: str, user_id: int | None) -> UserProfileDTO:
        try:
            user = self.user_repository.get(username)

        except NotFoundException:
            raise NotFoundException(f'Esse usuário não existe.')

        try:
            user_profile_entity = self.user_profile_repository.get(user_id=user.id)
            followers, following = self.user_repository.relations_count(user.id)
            posts = self.user_profile_repository.posts(user_profile_entity.id)
            if user_id != None:
                following_ids = self.user_repository.following_ids(user_id)
            else:
                following_ids = []

            user_dto = UserDTO(user_profile_entity.user, followers, following, user_profile_entity.user.id in following_ids)
            user_profile_dto = UserProfileDTO(user_profile_entity, user_dto, posts)
        
        except NotFoundException:
            raise NotFoundException(f'Esse perfil não existe.')
        
        except Exception:
            raise Exception('Ocorreu um erro ao buscar o perfil.')
        
        return user_profile_dto
    

class UpdateUserProfileUseCase:
    def __init__(self, user_profile_repository: UserProfileRepository, user_repository: UserRepository) -> None:
        self.user_profile_repository = user_profile_repository
        self.user_repository = user_repository

    def execute(self, user_id: int, name: str, profile_photo: str, website_url: str, bio: str, about: str, date_of_birth: date) -> UserProfileDTO:

        if not self.user_profile_repository.exists(user_id=user_id):
            raise NotFoundException(f'Esse perfil não existe.')
        
        try:
            updated_user_profile_entity = self.user_profile_repository.update(
                user_id,
                name,
                profile_photo,
                website_url,
                bio,
                about,
                date_of_birth
            )

        except Exception as err:
            raise Exception('Ocorreu um erro ao atualizar o perfil.')
        
        try:
            followers, following = self.user_repository.relations_count(updated_user_profile_entity.user.id)
            user_dto = UserDTO(updated_user_profile_entity.user, followers, following)
            user_profile_dto = UserProfileDTO(updated_user_profile_entity, user_dto)
            
        except Exception:
            raise Exception('Ocorreu um erro ao busca o perfil atualizado.')
        
        return user_profile_dto
