from api.domain.entities.post_tag import PostTag
from api.infrastructure.adapters.repositories.post_tag import PostTagRepository
from api.errors import NotFoundException, AlreadyExistsException

class CreatePostTagUseCase:
    def __init__(self, post_tag_repository: PostTagRepository) -> None:
        self.post_tag_repository = post_tag_repository

    def execute(self, name: str, slug: str) -> PostTag:
        if self.post_tag_repository.exists(slug=slug):
            raise AlreadyExistsException('Já existe uma tag com esse nome.')

        post_tag = PostTag(name, slug)

        try:
            created_post_tag = self.post_tag_repository.save(post_tag)

        except Exception:
            raise Exception('Ocorreu um erro ao criar a tag.')

        return created_post_tag
    

class ListTagsUseCase:
    def __init__(self, post_tag_repository: PostTagRepository) -> None:
        self.post_tag_repository = post_tag_repository
    
    def execute(self) -> list[PostTag]:
        try:
            post_tags = self.post_tag_repository.list_all()

        except Exception:
            raise Exception('Ocorreu um erro ao buscar as tags.')
        
        return post_tags


class GetPostTagUseCase:
    def __init__(self, post_tag_repository: PostTagRepository) -> None:
        self.post_tag_repository = post_tag_repository

    def execute(self, slug: str) -> PostTag:
        try:
            post_tag = self.post_tag_repository.get(slug=slug)

        except NotFoundException:
            raise NotFoundException('Essa tag não existe.')
        
        return post_tag