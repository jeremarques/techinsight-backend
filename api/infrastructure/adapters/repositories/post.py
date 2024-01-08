import pytz
from datetime import datetime
from django.db.models import F
from api.domain.entities.post import Post as PostEntity
from api.models.post import Post as PostModel
from api.errors import NotFoundException, IntegrityError

class PostRepository:
    def __init__(self):
        dt_now = datetime.now(pytz.timezone('America/Fortaleza'))
        self.dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

    def save(self, post: PostEntity) -> PostEntity:
        post_model = PostModel.from_entity(post)

        try: 
            post_model.save()
        
        except IntegrityError:
            post.set_public_id()
            self.save(post)

        post_entity = post_model.to_entity()

        return post_entity
    
    def get(self, *args, **kwargs) -> PostEntity:
        try:
            post_model = PostModel.objects.get(**kwargs)

        except PostModel.DoesNotExist:
            raise NotFoundException

        post_entity = post_model.to_entity()

        return post_entity
    
    def update(self, id: str, title: str, content: str) -> PostEntity:
        post_model = PostModel.objects.filter(id=id)
        post_model.update(title=title, content=content, updated_at=self.dt_local)
        
        post_updated_entity = self.get(id=id)

        return post_updated_entity
    
    def delete(self, id: str) -> None:
        post_tag_model = PostModel.objects.get(id=id)
        post_tag_model.delete()

        return None
    
    def likes(self, post_id: str) -> int:
        post = PostModel.objects.get(id=post_id)
        likes = post.likes.count()

        return likes

    def comments(self, post_id: str) -> int:
        post = PostModel.objects.get(id=post_id)
        comments = post.comments.count()

        return comments
    
    def filter(self, *args, **kwargs) -> list[PostEntity]:
        posts_models = PostModel.objects.filter(*args, **kwargs)
        posts_entities = [post_model.to_entity() for post_model in posts_models]

        return posts_entities
    
    def exists(self, *args, **kwargs) -> bool:
        post = PostModel.objects.filter(**kwargs)

        if post.exists():
            return True
        else:
            return False
    
    
    
