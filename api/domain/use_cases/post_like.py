from api.domain.entities.post_like import PostLike
from api.infrastructure.adapters.repositories.post_like import PostLikeRepository
from api.infrastructure.adapters.repositories.post import PostRepository
from api.errors import NotFoundException, AlreadyExistsException, ForbiddenException

class CreatePostLikeUseCase:
    def __init__(self, post_like_repository: PostLikeRepository, post_repository: PostRepository) -> None:
        self.post_like_repository = post_like_repository
        self.post_repository = post_repository

    def execute(self, profile_id: int, public_id: str) -> PostLike:

        try:
            post = self.post_repository.get(public_id=public_id)

        except NotFoundException:
            raise NotFoundException('Esse post não existe.')
        
        if post.profile.id == profile_id:
            raise ForbiddenException('Você não pode dar like no seu próprio post.')

        if self.post_like_repository.exists(profile_id=profile_id, post_id=post.id):
            raise AlreadyExistsException(f'Você já deu like nessa postagem.')

        post_like = PostLike(profile_id, post.id)

        try:
            created_post_like = self.post_like_repository.save(post_like)

        except Exception:
            raise Exception('Ocorreu um erro ao dar like na postagem.')

        return created_post_like
    

class DeletePostLikeUseCase:
    def __init__(self, post_like_repository: PostLikeRepository, post_repository: PostRepository) -> None:
        self.post_like_repository = post_like_repository
        self.post_repository = post_repository

    def execute(self, profile_id: int, public_id: str) -> None:

        try:
            post = self.post_repository.get(public_id=public_id)

        except NotFoundException:
            raise NotFoundException('Esse post não existe.')

        if not self.post_like_repository.exists(profile_id=profile_id, post_id=post.id):
            raise NotFoundException(f'Você não deu like nessa postagem.')
        
        try:
            post_like = self.post_like_repository.delete(profile_id, post.id)

        except NotFoundException:
            raise NotFoundException(f'Ocorreu um erro ao retirar o like da postagem.')
        
        return post_like