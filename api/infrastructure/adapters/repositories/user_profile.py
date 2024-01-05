import pytz
from datetime import date, datetime
from api.domain.entities.user_profile import UserProfile as UserProfileEntity
from api.models.user_profile import UserProfile as UserProfileModel
from api.errors import NotFoundException

class UserProfileRepository:
    def __init__(self):
        dt_now = datetime.now(pytz.timezone('America/Fortaleza'))
        self.dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

    def save(self, profile: UserProfileEntity) -> UserProfileEntity:
        profile_model = UserProfileModel.from_entity(profile)
        profile_model.save()
        profile_entity = profile_model.to_entity()

        return profile_entity
    
    def get(self, user_id: int) -> UserProfileEntity:
        try:
            profile_model = UserProfileModel.objects.get(user=user_id)

        except UserProfileModel.DoesNotExist as err:
            raise NotFoundException(f'O perfil do usuário {user_id} não foi encontrado.')

        profile_entity = profile_model.to_entity()

        return profile_entity

    def update(self, user_id: int, name: str, profile_photo: str, website_url: str, bio: str, about: str, date_of_birth: date) -> UserProfileEntity:

        profile_model = UserProfileModel.objects.filter(user=user_id)

        profile_model.update(
            name=name,
            profile_photo=profile_photo,
            website=website_url,
            bio=bio,
            about=about,
            date_of_birth=date_of_birth,
            updated_at=self.dt_local
        )
        profile_updated_entity = self.get(user_id)

        return profile_updated_entity
        
    def exists(self, user_id: int) -> bool:
        profile = UserProfileModel.objects.filter(user_id=user_id)

        if profile.exists():
            return True
        else:
            return False

