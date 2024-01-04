from api.domain.entities.post_tag import PostTag
from api.infrastructure.adapters.repositories.post_tag import PostTagRepository
from api.errors import NotFoundException, AlreadyExistsException

class CreatePostTagUseCase:
    def __init__(self, post_tag_repository: PostTagRepository) -> None:
        self.post_tag_repository = post_tag_repository

    def execute(self, name: str, slug: str) -> PostTag:
        if self.post_tag_repository.exists(slug):
            raise AlreadyExistsException(f'Já existe uma tag com nome {name}')

        post_tag = PostTag(name, slug)
        created_post_tag = self.post_tag_repository.save(post_tag)

        return created_post_tag
    

class GetPostTagUseCase:
    def __init__(self, post_tag_repository: PostTagRepository) -> None:
        self.post_tag_repository = post_tag_repository

    def execute(self, slug: str) -> PostTag:
        try:
            post_tag = self.post_tag_repository.get(slug)

        except NotFoundException as err:
            raise err
        
        return post_tag