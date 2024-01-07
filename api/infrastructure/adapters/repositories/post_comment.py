import pytz
from datetime import datetime
from api.domain.entities.post_comment import PostComment as PostCommentEntity
from api.models.post_comment import PostComment as PostCommentModel

class PostCommentRepository:
    def __init__(self):
        dt_now = datetime.now(pytz.timezone('America/Fortaleza'))
        self.dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

    def save(self, post_comment: PostCommentEntity) -> PostCommentEntity:
        post_comment_model = PostCommentModel.from_entity(post_comment)
        post_comment_model.save()
        post_comment_entity = post_comment_model.to_entity()

        return post_comment_entity
    
    def list_by_post(self, post_id: str) -> list[PostCommentEntity]:
        post_comments_models = PostCommentModel.objects.filter(post_id=post_id)
        post_comments_entities = [post_comment_model.to_entity() for post_comment_model in post_comments_models]

        return post_comments_entities

    def update(self, comment_id: int, content: str) -> PostCommentEntity:
        post_comment_model = PostCommentModel.objects.filter(id=comment_id)
        post_comment_model.update(content=content)

        updated_post_comment = PostCommentModel.objects.get(id=comment_id).to_entity()
        return updated_post_comment
    
    def delete(self, comment_id: int) -> None:
        post_comment_model = PostCommentModel.objects.get(id=comment_id)
        post_comment_model.delete()

        return None
    
    def exists(self, *args, **kwargs) -> bool:
        post_comment = PostCommentModel.objects.filter(**kwargs)

        if post_comment.exists():
            return True
        else:
            return False
    
    
    
