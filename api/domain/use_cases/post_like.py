from api.domain.entities.post_like import PostLike
from api.infrastructure.adapters.repositories.post_like import PostLikeRepository
from api.infrastructure.adapters.repositories.post import PostRepository
from api.errors import NotFoundException, AlreadyExistsException

class CreatePostLikeUseCase:
    def __init__(self, post_like_repository: PostLikeRepository, post_repository: PostRepository) -> None:
        self.post_like_repository = post_like_repository
        self.post_repository = post_repository

    def execute(self, profile_id: int, post_id: str) -> PostLike:
        if not self.post_repository.exists(id=post_id):
            raise NotFoundException('Este post não existe.')

        if self.post_like_repository.exists(profile_id=profile_id, post_id=post_id):
            raise AlreadyExistsException(f'Você já deu like nessa postagem')

        post_like = PostLike(profile_id, post_id)

        try:
            created_post_like = self.post_like_repository.save(post_like)

        except Exception:
            raise Exception('Ocorreu um erro ao dar like na postagem.')

        return created_post_like
    

class DeletePostLikeUseCase:
    def __init__(self, post_like_repository: PostLikeRepository) -> None:
        self.post_like_repository = post_like_repository

    def execute(self, profile_id: int, post_id: str) -> None:
        if not self.post_like_repository.exists(profile_id=profile_id, post_id=post_id):
            raise NotFoundException(f'Você não deu like nessa postagem')
        
        try:
            post_like = self.post_like_repository.delete(profile_id, post_id)

        except NotFoundException:
            raise NotFoundException(f'Ocorreu um erro ao retirar o like da postagem.')
        
        return post_like