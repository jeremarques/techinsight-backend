import pytz
from datetime import date, datetime
from uuid import UUID
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
    
    def get(self, *args, **kwargs) -> UserProfileEntity:
        try:
            profile_model = UserProfileModel.objects.get(*args, **kwargs)

        except UserProfileModel.DoesNotExist:
            raise NotFoundException

        profile_entity = profile_model.to_entity()

        return profile_entity
    
    def liked_posts_ids(self, profile_id: int) -> list[UUID]:
        profile = UserProfileModel.objects.get(id=profile_id)
        likes = profile.likes.all()
        posts_ids = [like.post_id for like in likes]

        return posts_ids
    
    def posts(self, profile_id: int | None) -> int:
        profile = UserProfileModel.objects.get(id=profile_id)
        posts = profile.posts.count()

        return posts

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
        profile_updated_entity = self.get(user=user_id)

        return profile_updated_entity
        
    def exists(self, *args, **kwargs) -> bool:
        profile = UserProfileModel.objects.filter(*args, **kwargs)

        if profile.exists():
            return True
        else:
            return False

