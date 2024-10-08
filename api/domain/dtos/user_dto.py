from api.domain.entities.user import User

class UserDTO:
    def __init__(self, user: User, followers: int = 0, following: int = 0, is_follower: bool = False):
        self.id = user.id
        self.username = user.username
        self.email = user.email
        self.full_name = user.full_name
        self.followers = followers
        self.following = following
        self.is_follower = is_follower
        self.is_active = user.is_active
        self.created_at = user.created_at
        self.updated_at = user.updated_at