import unittest
from datetime import datetime

from api.domain.entities.post_like import PostLike

class TestPostLikeDomainUnit(unittest.TestCase):

    def test_constructor(self):
        post_like = PostLike(
            1,
            '3a29514792a84ee4930e864549ef8684',
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )
        self.assertEqual(post_like.profile_id, 1)
        self.assertEqual(post_like.post_id, '3a29514792a84ee4930e864549ef8684')
        self.assertEqual(post_like.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))

