import pytz
from datetime import datetime
from api.domain.entities.post_tag import PostTag as PostTagEntity
from api.models.post_tag import PostTag as PostTagModel
from api.errors import NotFoundException

class PostTagRepository:
    def __init__(self):
        dt_now = datetime.now(pytz.timezone('America/Fortaleza'))
        self.dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

    def save(self, post_tag: PostTagEntity) -> PostTagEntity:
        post_tag_model = PostTagModel.from_entity(post_tag)
        post_tag_model.save()
        post_tag_entity = post_tag_model.to_entity()

        return post_tag_entity
    
    def get(self, *args, **kwargs) -> PostTagEntity:
        try:
            post_tag_model = PostTagModel.objects.get(**kwargs)

        except PostTagModel.DoesNotExist as err:
            raise NotFoundException
        
        post_tag_entity = post_tag_model.to_entity()

        return post_tag_entity
    
    def list_all(self) -> list[PostTagEntity]:
        tags_models = PostTagModel.objects.all()
        tags_entities = [tag.to_entity() for tag in tags_models]

        return tags_entities

    def delete(self, id: int) -> None:
        post_tag_model = PostTagModel.objects.get(id=id)
        post_tag_model.delete()

        return None
    
    def exists(self, *args, **kwargs) -> bool:
        post_tag = PostTagModel.objects.filter(**kwargs)

        if post_tag.exists():
            return True
        else:
            return False
    
    
    
