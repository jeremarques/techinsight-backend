from uuid import UUID
from api.domain.dtos.full_post_dto import FullPostDTO
from api.domain.dtos.user_dto import UserDTO
from api.domain.dtos.user_profile_dto import UserProfileDTO
from api.domain.entities.post import Post
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user import UserRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.repositories.post_tag import PostTagRepository
from api.domain.dtos.post_dto import PostDTO
from api.errors import NotFoundException, ForbiddenException


class CreatePostUseCase:
    def __init__(self, post_repository: PostRepository, user_profile_repository: UserProfileRepository, post_tag_repository: PostTagRepository) -> None:
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository
        self.post_tag_repository = post_tag_repository

    def execute(self, user_id: int, title: str, slug: str, content: str, tag_id: int) -> PostDTO:

        try:
            profile = self.user_profile_repository.get(user_id=user_id)

        except NotFoundException:
            raise NotFoundException('O perfil do usuário que você buscou não existe.')
        
        try:
            tag = self.post_tag_repository.get(id=tag_id)

        except NotFoundException:
            raise NotFoundException('A tag que você escolheu não existe.')

        post = Post(
            profile,
            title,
            slug,
            content,
            tag
        )
        
        try:
            post_entity = self.post_repository.save(post)

        except Exception:
            raise Exception('Ocorreu um erro ao salvar o post.')
        
        post = PostDTO(post_entity, 0, 0)

        return post
    

class GetPostUseCase:
    def __init__(self, post_repository: PostRepository, user_profile_repository: UserProfileRepository, user_repository: UserRepository) -> None:
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository
        self.user_repository = user_repository

    def execute(self, public_id: str, user_profile_id: int | None) -> FullPostDTO:
        try:
            post_entity = self.post_repository.get(public_id=public_id)
            likes_counter = self.post_repository.likes(post_entity.id)
            comments_counter = self.post_repository.comments(post_entity.id)
            post_user_profile_entity = post_entity.profile
            followers, following = self.user_repository.relations_count(post_user_profile_entity.user.id)
            
            if user_profile_id != None:
                user_profile_entity = self.user_profile_repository.get(id=user_profile_id)
                user_liked_posts_ids = self.user_profile_repository.liked_posts_ids(user_profile_id)
                following_ids = self.user_repository.following_ids(user_profile_entity.user.id)

            else:
                user_liked_posts_ids = []
                following_ids = []

        except NotFoundException:
            raise NotFoundException(f'Esse post não existe.')
        
        except Exception:
            raise Exception('Ocorreu um erro ao buscar o post.')
        
        post_user_dto = UserDTO(post_user_profile_entity.user, followers, following, post_user_profile_entity.user.id in following_ids)
        user_profile_dto = UserProfileDTO(post_user_profile_entity, post_user_dto)
        post = FullPostDTO(post_entity, user_profile_dto, likes_counter, comments_counter, post_entity.id in user_liked_posts_ids)

        return post
    

class ListAllPostsUseCase:
    def __init__(self, post_repository: PostRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, user_profile_id: int | None) -> list[PostDTO]:
        try:
            posts_entities = self.post_repository.all()

            if user_profile_id != None:
                user_liked_posts_ids = self.user_profile_repository.liked_posts_ids(user_profile_id)
            else:
                user_liked_posts_ids = []

            posts = []

            for post_entity in posts_entities:
                likes_counter = self.post_repository.likes(post_entity.id)
                comments_counter = self.post_repository.comments(post_entity.id)
                post = PostDTO(post_entity, likes_counter, comments_counter, post_entity.id in user_liked_posts_ids)
                posts.append(post)

        except Exception:
            raise Exception('Ocorreu um erro ao buscar os posts.')

        return posts


class ListProfilePostsUseCase:
    def __init__(self, post_repository: PostRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, profile_id: int, user_profile_id: int | None) -> list[PostDTO]:
        if not self.user_profile_repository.exists(id=profile_id):
            raise NotFoundException('Esse perfil não existe.')
        
        try:
            posts_entities = self.post_repository.filter(profile_id=profile_id)

            if user_profile_id != None:
                user_liked_posts_ids = self.user_profile_repository.liked_posts_ids(user_profile_id)
            else:
                user_liked_posts_ids = []

            posts = []

            for post_entity in posts_entities:
                likes_counter = self.post_repository.likes(post_entity.id)
                comments_counter = self.post_repository.comments(post_entity.id)
                post = PostDTO(post_entity, likes_counter, comments_counter, post_entity.id in user_liked_posts_ids)
                posts.append(post)

        except Exception:
            raise Exception('Ocorreu um erro ao buscar os posts.')
        
        return posts
    

class ListPostsByTag:
    def __init__(self, post_repository: PostRepository, post_tag_repository: PostTagRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_repository = post_repository
        self.post_tag_repository = post_tag_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, tag_slug: str, user_profile_id: int | None) -> list[PostDTO]:

        try:
            tag = self.post_tag_repository.get(slug=tag_slug)
            posts_entities = self.post_repository.filter(tag_id=tag.id)

            if user_profile_id != None:
                user_liked_posts_ids = self.user_profile_repository.liked_posts_ids(user_profile_id)
            else:
                user_liked_posts_ids = []

            posts = []

            for post_entity in posts_entities:
                likes_counter = self.post_repository.likes(post_entity.id)
                comments_counter = self.post_repository.comments(post_entity.id)
                post = PostDTO(post_entity, likes_counter, comments_counter, post_entity.id in user_liked_posts_ids)
                posts.append(post)

        except NotFoundException:
            raise NotFoundException('Essa tag não existe.')
        
        except Exception:
            raise Exception('Ocorreu um erro ao buscar os posts.')
        
        return posts
        

class UpdatePostUseCase:
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, profile_id: int, post_id: str, title: str, content: str) -> PostDTO:
        if not self.post_repository.exists(id=post_id):
            raise NotFoundException('Esse post não existe.')
        
        if not self.post_repository.exists(id=post_id, profile_id=profile_id):
            raise ForbiddenException('Você não pode editar um post de outro usuário.')
        
        try:
            updated_post_entity = self.post_repository.update(UUID(post_id), title, content)
            likes_counter = self.post_repository.likes(UUID(post_id))
            comments_counter = self.post_repository.comments(UUID(post_id))

        except Exception:
            raise Exception('Ocorreu um erro ao editar o post.')
        
        post = PostDTO(updated_post_entity, likes_counter, comments_counter)

        return post


class DeletePostUseCase:
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, profile_id: int, post_id: str) -> None:
        if not self.post_repository.exists(id=post_id):
            raise NotFoundException('Esse post não existe.')
        
        if not self.post_repository.exists(id=post_id, profile_id=profile_id):
            raise ForbiddenException('Você não pode excluir um post de outro usuário.')
        
        try:
            self.post_repository.delete(UUID(post_id))

        except Exception:
            raise Exception('Ocorreu um erro ao tentar excluir o post.')
        
        return None
