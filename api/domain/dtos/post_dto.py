from api.domain.entities.post import Post

class PostDTO:
    def __init__(self, post: Post, likes: int, comments: int):
        self.id = post.id
        self.public_id = post.public_id
        self.profile = post.profile
        self.title = post.title
        self.slug = post.slug
        self.content = post.slug
        self.tag = post.tag
        self.likes = likes
        self.comments = comments
        self.created_at = post.created_at
        self.updated_at = post.updated_at
    
