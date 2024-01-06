import unittest

from api.domain.entities.post import Post
from api.domain.entities.user_profile import UserProfile
from api.domain.entities.user import User
from api.domain.entities.post_tag import PostTag
from api.domain.use_cases.post import CreatePostUseCase, GetPostUseCase, UpdatePostUseCase


class PostMockRepository:
    called_times = 0
    
    def save(self, post: Post):
        self.called_times += 1
        
        return Post(
            profile=post.profile,
            title=post.title,
            slug=post.slug,
            content=post.content,
            tag=post.tag,
            created_at=post.created_at
        )
    
    def get(self, *args, **kwargs):
        self.called_times += 1

        tag = PostTag(
            id=2,
            name='Test tag',
            slug='test-tag',
        )

        user_data = {
            'id': 1,
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        user_profile = UserProfile(id=1, user=User(**user_data), name=user_data.get('full_name'))

        return Post(
            public_id=kwargs.get('public_id'),
            profile=user_profile,
            title='Post test',
            slug='post-test',
            content='Post content here',
            tag=tag
        )
    
    def update(self, id: str, title: str, content: str):
        self.called_times += 1

        tag = PostTag(
            id=2,
            name='Test tag',
            slug='test-tag',
        )
        
        user_data = {
            'id': 1,
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }
        user_profile = UserProfile(id=1, user=User(**user_data), name=user_data.get('full_name'))
        

        return Post(
            id=id,
            profile=user_profile,
            title=title,
            slug='post-test',
            content=content,
            tag=tag
        )

    def exists(self, *args, **kwargs):
        self.called_times += 1

        return True
    

class UserProfileMockRepository:
    called_times = 0
    
    def get(self, *args, **kwargs):
        self.called_times += 1

        user = {
            'id': 1,
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        return UserProfile(id=kwargs.get('user_id'), user=User(**user), name=user.get('full_name'))


class PostTagMockRepository:
    called_times = 0
    
    def get(self, *args, **kwargs):
        self.called_times += 1

        return PostTag(
            id=kwargs.get('id'),
            name='Test tag',
            slug='test-tag',
        )


class TestPostUseCases(unittest.TestCase):
    def test_should_create_post(self):
        post_mock_repository = PostMockRepository()
        user_profile_mock_repository = UserProfileMockRepository()
        post_tag_mock_repository = PostTagMockRepository()

        use_case = CreatePostUseCase(post_mock_repository, user_profile_mock_repository, post_tag_mock_repository)
        result = use_case.execute(1, 'Test Post', 'test-post', 'Post content here', 2)

        self.assertEqual(result.profile.name, 'Jeremias Marques')
        self.assertEqual(result.profile.id, 1)
        self.assertEqual(result.title, 'Test Post')
        self.assertEqual(result.slug, 'test-post')
        self.assertEqual(result.content, 'Post content here')
        self.assertEqual(result.tag.id, 2)
        self.assertEqual(post_mock_repository.called_times, 1)
        self.assertEqual(user_profile_mock_repository.called_times, 1)
        self.assertEqual(post_tag_mock_repository.called_times, 1)

    def test_should_return_post(self):
        post_mock_repository = PostMockRepository()

        use_case = GetPostUseCase(post_mock_repository)
        result = use_case.execute('dbd83da73b0c47')

        self.assertEqual(result.public_id, 'dbd83da73b0c47')
        self.assertEqual(result.slug, 'post-test')
        self.assertEqual(result.profile.id, 1)
        self.assertEqual(result.profile.name, 'Jeremias Marques')
        self.assertEqual(result.tag.id, 2)
        self.assertEqual(result.tag.slug, 'test-tag')
        self.assertEqual(post_mock_repository.called_times, 1)

    def test_should_update_post(self):
        post_mock_repository = PostMockRepository()

        use_case = UpdatePostUseCase(post_mock_repository)
        result = use_case.execute(1, '3a29514792a84ee4930e864549ef8684', 'Updated title', 'Updated content')

        self.assertEqual(result.id, '3a29514792a84ee4930e864549ef8684')
        self.assertEqual(result.profile.id, 1)
        self.assertEqual(result.title, 'Updated title')
        self.assertEqual(result.content, 'Updated content')
        self.assertEqual(post_mock_repository.called_times, 3)

