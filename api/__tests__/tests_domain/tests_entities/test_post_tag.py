import unittest
from datetime import datetime

from api.domain.entities.post_tag import PostTag

class TestPostTagDomainUnit(unittest.TestCase):

    def test_constructor(self):
        relationship = PostTag(
            'Tag name',
            'tag-name',
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )
        self.assertEqual(relationship.name, 'Tag name')
        self.assertEqual(relationship.slug, 'tag-name')
        self.assertEqual(relationship.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))

