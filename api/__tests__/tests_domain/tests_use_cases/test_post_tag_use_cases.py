import unittest

from api.domain.entities.post_tag import PostTag
from api.domain.use_cases.post_tag import CreatePostTagUseCase, GetPostTagUseCase

class PostTagMockRepository:
    called_times = 0
    
    def save(self, post_tag: PostTag):
        self.called_times += 1
        
        return PostTag(
            name=post_tag.name,
            slug=post_tag.slug,
            created_at=post_tag.created_at
        )
    
    def get(self, slug: str):
        self.called_times += 1

        return PostTag(
            name='Test tag',
            slug='test-tag',
        )

    def exists(self, slug: str):
        self.called_times += 1

        return False


class TestRelationshipUseCases(unittest.TestCase):
    def test_create_post_tag(self):
        post_tag_mock_repository = PostTagMockRepository()

        relationship_data = {
            'name': 'Test tag',
            'slug': 'test-tag'
        }

        use_case = CreatePostTagUseCase(post_tag_mock_repository)
        result = use_case.execute(**relationship_data)


        self.assertEqual(result.name, 'Test tag')
        self.assertEqual(result.slug, 'test-tag')
        self.assertEqual(post_tag_mock_repository.called_times, 2)

    def test_should_return_post_tag(self):
        post_tag_mock_repository = PostTagMockRepository()

        use_case = GetPostTagUseCase(post_tag_mock_repository)

        result = use_case.execute('test-tag')

        self.assertEqual(result.name, 'Test tag')
        self.assertEqual(result.slug, 'test-tag')
        self.assertEqual(post_tag_mock_repository.called_times, 1)