import unittest
from datetime import datetime

from api.domain.entities.post_tag import PostTag

class TestPostTagDomainUnit(unittest.TestCase):

    def test_constructor(self):
        post_tag = PostTag(
            'Tag name',
            'tag-name',
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )
        self.assertEqual(post_tag.name, 'Tag name')
        self.assertEqual(post_tag.slug, 'tag-name')
        self.assertEqual(post_tag.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))
        self.assertIsNone(post_tag.updated_at)

