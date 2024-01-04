from datetime import date
from api.domain.entities.user_profile import UserProfile as UserProfileEntity
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.errors import NotFoundException


class CreateUserProfileUseCase:
    def __init__(self, repository: UserProfileRepository) -> None:
        self.repository = repository

    def execute(self, user_id: int, name: str) -> UserProfileEntity:
        user_profile = UserProfileEntity(user_id=user_id, name=name)
        created_user_profile_entity = self.repository.save(user_profile)

        return created_user_profile_entity


class GetUserProfileUseCase:
    def __init__(self, repository: UserProfileRepository) -> None:
        self.repository = repository

    def execute(self, user_id: int) -> UserProfileEntity:
        try:
            user_profile_entity = self.repository.get(user_id)
        
        except NotFoundException as err:
            raise err
        
        return user_profile_entity
    

class UpdateUserProfileUseCase:
    def __init__(self, repository: UserProfileRepository) -> None:
        self.repository = repository

    def execute(self, user_id: int, name: str, profile_photo: str, website_url: str, bio: str, about: str, date_of_birth: date) -> UserProfileEntity:

        if not self.repository.exists(user_id):
            raise NotFoundException(f'O perfil com do usuário {user_id} não foi encontrado.')
        
        updated_user = self.repository.update(
            user_id,
            name,
            profile_photo,
            website_url,
            bio,
            about,
            date_of_birth
        )

        return updated_user
