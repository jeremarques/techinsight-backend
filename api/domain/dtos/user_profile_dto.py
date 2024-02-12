from .user_dto import UserDTO
from api.domain.entities.user_profile import UserProfile

class UserProfileDTO:
    def __init__(self, user_profile: UserProfile, user: UserDTO, posts: int = 0):
        self.id = user_profile.id
        self.user = user
        self.name = user_profile.name
        self.profile_photo = user_profile.profile_photo
        self.posts = posts
        self.website_url = user_profile.website_url
        self.bio = user_profile.bio
        self.about = user_profile.about
        self.date_of_birth = user_profile.date_of_birth
        self.created_at = user_profile.created_at
        self.updated_at = user_profile.updated_at