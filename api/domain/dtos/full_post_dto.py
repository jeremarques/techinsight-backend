from api.domain.entities.post import Post
from api.domain.dtos.user_profile_dto import UserProfileDTO

class FullPostDTO:
    def __init__(self, post: Post, profile: UserProfileDTO, likes: int, comments: int, is_liked: bool = False):
        self.id = post.id
        self.public_id = post.public_id
        self.profile = profile
        self.title = post.title
        self.slug = post.slug
        self.content = post.content
        self.tag = post.tag
        self.is_liked = is_liked
        self.likes = likes
        self.comments = comments
        self.created_at = post.created_at
        self.updated_at = post.updated_at
    
