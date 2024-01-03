import unittest
from datetime import datetime

from api.domain.entities.relationship import Relationship

class TestRelationshipDomainUnit(unittest.TestCase):

    def test_constructor(self):
        relationship = Relationship(
            2,
            7,
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )
        self.assertEqual(relationship.follower_id, 2)
        self.assertEqual(relationship.followed_id, 7)
        self.assertEqual(relationship.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))

