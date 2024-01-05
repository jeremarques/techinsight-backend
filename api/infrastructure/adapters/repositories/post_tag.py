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
    
    def get(self, tag_slug: str) -> PostTagEntity:
        try:
            post_tag_model = PostTagModel.objects.get(slug=tag_slug)

        except PostTagModel.DoesNotExist as err:
            raise NotFoundException(f'A tag {tag_slug} não foi encontrada.')

        post_tag_entity = post_tag_model.to_entity()

        return post_tag_entity
    
    def delete(self, id: int) -> None:
        post_tag_model = PostTagModel.objects.get(id=id)
        post_tag_model.delete()

        return None
    
    def exists(self, slug: str):
        post_tag = PostTagModel.objects.filter(slug=slug)

        if post_tag.exists():
            return True
        else:
            return False
    
    
    
