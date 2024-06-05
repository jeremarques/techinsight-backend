from api.domain.entities.post_comment import PostComment
from api.infrastructure.adapters.repositories.post_comment import PostCommentRepository
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.errors import NotFoundException, ForbiddenException


class CreatePostCommentUseCase:
    def __init__(self, post_comment_repository: PostCommentRepository, post_repository: PostRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_comment_repository = post_comment_repository
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, profile_id: int, public_id: str, content: str) -> PostComment:

        try:
            post = self.post_repository.get(public_id=public_id)

        except NotFoundException:
            raise NotFoundException('Esse post não existe.')

        try: 
            user_profile = self.user_profile_repository.get(id=profile_id)

        except NotFoundException as err:
            raise err

        post_comment = PostComment(user_profile, content, post.id)

        try:
            post_comment = self.post_comment_repository.save(post_comment)

        except Exception as err:
            raise Exception('Ocorreu um erro ao adicionar o comentário.')

        return post_comment
    

class ListPostCommentsUseCase:
    def __init__(self, post_comment_repository: PostCommentRepository, post_repository: PostRepository) -> None:
        self.post_comment_repository = post_comment_repository
        self.post_repository = post_repository

    def execute(self, public_id: str) -> list[PostComment]:

        try:
            post = self.post_repository.get(public_id=public_id)

        except NotFoundException:
            raise NotFoundException('Esse post não existe.')
        
        try:
            comments = self.post_comment_repository.list_by_post(post.id)

        except Exception:
            raise Exception('Ocorreu um erro ao buscar os comentários.')
        
        return comments


class UpdatePostCommentUseCase:
    def __init__(self, post_comment_repository: PostCommentRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_comment_repository = post_comment_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, profile_id: int, comment_id: int, content: str) -> PostComment:

        if not self.post_comment_repository.exists(id=comment_id):
            raise NotFoundException('Esse comentário não existe.')

        if not self.post_comment_repository.exists(id=comment_id, profile_id=profile_id):
            raise ForbiddenException('Você não pode editar um comentário de outro usuário.')
        
        try:
            updated_post_comment = self.post_comment_repository.update(comment_id, content)

        except Exception as err:
            print(err)
            raise Exception('Ocorreu um erro ao editar o comentário.')
        
        return updated_post_comment

    
class DeletePostCommentUseCase:
    def __init__(self, post_comment_repository: PostCommentRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_comment_repository = post_comment_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, profile_id: int, comment_id: int) -> None:

        if not self.post_comment_repository.exists(id=comment_id):
            raise NotFoundException('Esse comentário não existe.')

        if not self.post_comment_repository.exists(id=comment_id, profile_id=profile_id):
            raise ForbiddenException('Você não pode excluir um comentário de outro usuário.')
        
        try:
            self.post_comment_repository.delete(comment_id)
        
        except Exception:
            raise Exception('Não foi possível excluir o comentário.')
        
        return None

