from api.domain.entities.post_comment import PostComment
from api.infrastructure.adapters.repositories.post_comment import PostCommentRepository
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.errors import NotFoundException, AlreadyExistsException


class CreatePostCommentUseCase:
    def __init__(self, post_comment_repository: PostCommentRepository, post_repository: PostRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_comment_repository = post_comment_repository
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, profile_id: int, post_id: str, content: str) -> PostComment:

        if not self.post_repository.exists(id=post_id):
            raise NotFoundException(f'Este post não existe')

        try: 
            user_profile = self.user_profile_repository.get(id=profile_id)

        except NotFoundException as err:
            raise err

        post_comment = PostComment(user_profile, post_id, content)

        try:
            post_comment = self.post_comment_repository.save(post_comment)

        except Exception as err:
            print(err)
            raise Exception('Ocorreu um erro ao adicionar o comentário.')

        return post_comment
    
