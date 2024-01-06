from datetime import date
from api.domain.entities.user_profile import UserProfile as UserProfileEntity
from api.domain.entities.user import User as UserEntity
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.repositories.user import UserRepository
from api.errors import NotFoundException


class CreateUserProfileUseCase:
    def __init__(self, user_profile_repository: UserProfileRepository) -> None:
        self.user_profile_repository = user_profile_repository

    def execute(self, user: UserEntity, name: str) -> UserProfileEntity:
        user_profile = UserProfileEntity(user=user, name=name)

        try:
            created_user_profile_entity = self.user_profile_repository.save(user_profile)

        except Exception:
            raise Exception('Erro ao criar o perfil do usuário.')

        return created_user_profile_entity


class GetUserProfileUseCase:
    def __init__(self, user_profile_repository: UserProfileRepository, user_repository: UserRepository) -> None:
        self.user_profile_repository = user_profile_repository
        self.user_repository = user_repository

    def execute(self, username: str) -> UserProfileEntity:
        try:
            user = self.user_repository.get(username)

        except NotFoundException as err:
            raise NotFoundException(f'Este usuário não existe.')

        try:
            user_profile_entity = self.user_profile_repository.get(user_id=user.id)
        
        except NotFoundException as err:
            raise NotFoundException(f'Este perfil não foi encontrado.')
        
        return user_profile_entity
    

class UpdateUserProfileUseCase:
    def __init__(self, user_profile_repository: UserProfileRepository) -> None:
        self.user_profile_repository = user_profile_repository

    def execute(self, user_id: int, name: str, profile_photo: str, website_url: str, bio: str, about: str, date_of_birth: date) -> UserProfileEntity:

        if not self.user_profile_repository.exists(user_id=user_id):
            raise NotFoundException(f'Este perfil não foi encontrado.')
        
        try:
            updated_user = self.user_profile_repository.update(
                user_id,
                name,
                profile_photo,
                website_url,
                bio,
                about,
                date_of_birth
            )

        except Exception:
            raise Exception('Ocorreu um erro ao atualizar o perfil.')

        return updated_user
