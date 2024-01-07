from api.domain.entities.post_like import PostLike as PostLikeEntity
from api.models.post_like import PostLike as PostLikeModel

class PostLikeRepository:

    def save(self, post_like: PostLikeEntity) -> PostLikeEntity:
        post_like_model = PostLikeModel.from_entity(post_like)
        post_like_model.save()
        post_like_entity = post_like_model.to_entity()

        return post_like_entity
    
    def delete(self, profile_id: int, post_id: str) -> None:
        post_like_model = PostLikeModel.objects.get(profile_id=profile_id, post_id=post_id)
        post_like_model.delete()

        return None
    
    def exists(self, *args, **kwargs):
        post_like = PostLikeModel.objects.filter(**kwargs)

        if post_like.exists():
            return True
        else:
            return False
    
    
    
