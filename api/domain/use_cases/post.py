from api.domain.entities.post import Post
from api.infrastructure.adapters.repositories.post import PostRepository
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
        
        try:
            post_entity = self.post_repository.save(post)

        except Exception:
            raise Exception('Ocorreu um erro ao salvar o post.')
        
        post = PostDTO(post_entity, 0, 0)

        return post
    

class GetPostUseCase:
    def __init__(self, post_repository: PostRepository, user_profile_repository: UserProfileRepository) -> None:
        self.post_repository = post_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, public_id: str, user_profile_id: int | None) -> PostDTO:
        try:
            post_entity = self.post_repository.get(public_id=public_id)
            likes_counter = self.post_repository.likes(post_entity.id)
            comments_counter = self.post_repository.comments(post_entity.id)

            if user_profile_id != None:
                user_liked_posts_ids = self.user_profile_repository.liked_posts_ids(user_profile_id)
            else:
                user_liked_posts_ids = []

        except NotFoundException:
            raise NotFoundException(f'O post não foi encontrado.')
        
        except Exception:
            raise Exception('Ocorreu um erro ao buscar o post.')
        
        post = PostDTO(post_entity, likes_counter, comments_counter, post_entity.id in user_liked_posts_ids)

        return post
    

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
            raise NotFoundException(f'Esta tag não foi encontrada.')
        
        except Exception:
            raise Exception('Ocorreu um erro ao buscar os posts.')
        
        return posts
        

class UpdatePostUseCase:
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, profile_id: int, post_id: str, title: str, content: str) -> PostDTO:
        if not self.post_repository.exists(id=post_id):
            raise NotFoundException(f'O post não existe.')
        
        if not self.post_repository.exists(id=post_id, profile_id=profile_id):
            raise ForbiddenException('Você não pode editar um post de outro usuário.')
        
        try:
            updated_post_entity = self.post_repository.update(post_id, title, content)
            likes_counter = self.post_repository.likes(post_id)
            comments_counter = self.post_repository.comments(post_id)

        except Exception:
            raise Exception('Ocorreu um erro ao editar o post.')
        
        post = PostDTO(updated_post_entity, likes_counter, comments_counter)

        return post


class DeletePostUseCase:
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, profile_id: int, post_id: str) -> None:
        if not self.post_repository.exists(id=post_id):
            raise NotFoundException('Este post não existe.')
        
        if not self.post_repository.exists(id=post_id, profile_id=profile_id):
            raise ForbiddenException('Você não pode excluir um post de outro usuário.')
        
        try:
            self.post_repository.delete(post_id)

        except Exception:
            raise Exception('Ocorreu um erro ao tentar excluir o post.')
        
        return None
