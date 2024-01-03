from datetime import date
from api.domain.entities.user_profile import UserProfile as UserProfileEntity
from api.models.profile import Profile as ProfileModel
from api.errors import NotFoundException

class ProfileRepository:
    def save(self, profile: UserProfileEntity) -> UserProfileEntity:
        profile_model = ProfileModel.from_entity(profile)
        profile_model.save()
        profile_entity = profile_model.to_entity()

        return profile_entity
    
    def get(self, user_id: int) -> UserProfileEntity:
        try:
            profile_model = ProfileModel.objects.get(user=user_id)
            profile_entity = profile_model.to_entity()

        except ProfileModel.DoesNotExist as err:
            raise NotFoundException(f'Não foi encontrado um perfil para o usuário {user_id}')

        return profile_entity

    def update(self, user_id: int, profile_photo: str, website_url: str, bio: str, about: str, date_of_birth: date) -> UserProfileEntity:

        profile_model = ProfileModel.objects.filter(user=user_id)

        if not profile_model.exists():
            raise NotFoundException(f'O profile com user_id {user_id} não foi encontrado.')

        profile_model.update(
            profile_photo=profile_photo,
            website_url=website_url,
            bio=bio,
            about=about,
            date_of_birth=date_of_birth
        )
        profile_updated_entity = self.get(user_id)

        return profile_updated_entity

