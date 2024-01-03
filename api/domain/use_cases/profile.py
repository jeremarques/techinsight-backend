from datetime import date
from api.domain.entities.profile import Profile as ProfileEntity
from api.infrastructure.adapters.repositories.profile import ProfileRepository
from api.errors import NotFoundException

class CreateProfileUseCase:
    def __init__(self, repository: ProfileRepository) -> None:
        self.repository = repository

    def execute(self, user_id: int, name: str) -> ProfileEntity:
        profile = ProfileEntity(user_id=user_id, name=name)
        created_profie_entity = self.repository.save(profile)

        return created_profie_entity


class GetProfileUseCase:
    def __init__(self, repository: ProfileRepository) -> None:
        self.repository = repository

    def execute(self, user_id: int) -> ProfileEntity:
        try:
            profile_entity = self.repository.get(user_id)

        except NotFoundException as err:
            raise err
        
        return profile_entity
    

class UpdateProfileUseCase:
    def __init__(self, repository: ProfileRepository) -> None:
        self.repository = repository

    def execute(self, user_id: int, profile_photo: str, website_url: str, bio: str, about: str, date_of_birth: date) -> ProfileEntity:

        try:
            updated_user = self.repository.update(
                user_id,
                profile_photo,
                website_url,
                bio,
                about,
                date_of_birth
            )

        except NotFoundException as err:
            raise err

        return updated_user
