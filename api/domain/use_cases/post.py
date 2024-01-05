from api.domain.entities.post import Post
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.repositories.post_tag import PostTagRepository
from api.errors import NotFoundException, AlreadyExistsException, IntegrityError

class CreatePostUseCase:
    def __init__(self, post_repository: PostRepository, user_profile_repository: UserProfileRepository, post_tag_repository: PostTagRepository) -> None:
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository
        self.post_tag_repository = post_tag_repository

    def execute(self, user_id: int, title: str, slug: str, content: str, tag_id: int) -> Post:

        try:
            profile = self.user_profile_repository.get(user_id=user_id)

        except NotFoundException:
            raise NotFoundException(f'O perfil do usuário {user_id} não foi encontrado.')
        
        try:
            tag = self.post_tag_repository.get(id=tag_id)

        except NotFoundException:
            raise NotFoundException(f'A tag {tag_id} não foi encontrada.')

        post = Post(
            profile,
            title,
            slug,
            content,
            tag
        )
        
        created_post = self.post_repository.save(post)

        return created_post
    

class GetPostUseCase:
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, public_id: str) -> Post:
        try:
            post = self.post_repository.get(public_id=public_id)

        except NotFoundException:
            raise NotFoundException(f'O post não foi encontrado.')
        
        return post
    
