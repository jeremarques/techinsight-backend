from api.domain.entities.post_comment import PostComment
from api.infrastructure.adapters.repositories.post_comment import PostCommentRepository
from api.errors import NotFoundException, AlreadyExistsException

class CreatePostCommentUseCase:
    def __init__(self, post_comment_repository: PostCommentRepository) -> None:
        self.post_comment_repository = post_comment_repository

    def execute(self, profile_id: int, post_id: str) -> PostComment:

        if self.post_comment_repository.exists(profile_id=profile_id, post_id=post_id):
            raise AlreadyExistsException(f'Você já deu like nessa postagem')

        post_comment = PostComment(profile_id, post_id)

        try:
            created_post_comment = self.post_comment_repository.save(post_comment)

        except Exception:
            raise Exception('Ocorreu um erro ao dar like na postagem.')

        return created_post_comment
    
