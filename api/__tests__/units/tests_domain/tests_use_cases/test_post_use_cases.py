import unittest

from api.domain.entities.post import Post
from api.domain.use_cases.post import CreatePostUseCase, GetPostUseCase


class PostMockRepository:
    called_times = 0
    
    def save(self, post_tag: Post):
        self.called_times += 1
        
        return Post(
            name=post_tag.name,
            slug=post_tag.slug,
            created_at=post_tag.created_at
        )
    
    def get(self, slug: str):
        self.called_times += 1

        return Post(
            name='Test tag',
            slug='test-tag',
        )

    def exists(self, slug: str):
        self.called_times += 1

        return False


class TestPostUseCases(unittest.TestCase):
    def _create_post(self):
        post_mock_repository = PostMockRepository()
        user_profile_mock_repository = PostMockRepository()
        post_tag_mock_repository = PostMockRepository()

        post_data = {
            'name': 'Test tag',
            'slug': 'test-tag'
        }

        use_case = CreatePostUseCase(post_tag_mock_repository)
        result = use_case.execute(**post_data)
