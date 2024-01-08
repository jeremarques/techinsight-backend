import unittest
from datetime import datetime

from api.domain.entities.post import Post
from api.domain.entities.user_profile import UserProfile
from api.domain.entities.user import User
from api.domain.entities.post_tag import PostTag

class TestPostLikeDomainUnit(unittest.TestCase):

    def test_constructor(self):
        user_data = {
            'id': 1,
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        user_profile = UserProfile(User(**user_data), name=user_data.get('full_name'))
        post_tag = PostTag(
            'Tag name',
            'tag-name',
        )

        post = Post(
            user_profile,
            'Post title',
            'post-title',
            'Post content here',
            post_tag,
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )
        
        self.assertEqual(post.profile.name, 'Jeremias Marques')
        self.assertEqual(post.profile.user.username, 'jeremias')
        self.assertEqual(post.profile.user.email, 'jeremias@gmail.com')
        self.assertEqual(post.profile.user.id, 1)
        self.assertEqual(post.title, 'Post title')
        self.assertEqual(post.slug, 'post-title')
        self.assertEqual(post.content, 'Post content here')
        self.assertEqual(post.tag.name, 'Tag name')
        self.assertEqual(post.tag.slug, 'tag-name')
        self.assertEqual(post.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))

