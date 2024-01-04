import unittest

from api.domain.entities.relationship import Relationship
from api.domain.use_cases.relationship import FollowUserUseCase, UnfollowUserUseCase

class RelationshipMockRepository:
    called_times = 0
    
    def save(self, relationship: Relationship):
        self.called_times += 1
        
        return Relationship(
            follower_id=relationship.follower_id,
            followed_id=relationship.followed_id,
            created_at=relationship.created_at
        )
    
    def delete(self, follower_id: int, followed_id: int):
        self.called_times += 1

        return None

    def is_following(self, follower_id: int, followed_id: int):
        self.called_times += 1

        if follower_id == 1 and followed_id == 2:        
            return False

        return True
    

class UserMockRepository:
    called_times = 0
    
    def exists(self, id: int):
        self.called_times += 1
        
        return True


class TestRelationshipUseCases(unittest.TestCase):
    def test_shoud_follow_user(self):
        relationship_mock_repository = RelationshipMockRepository()
        user_mock_repository = UserMockRepository()

        relationship_data = {
            "follower_id": 1,
            "followed_id": 2
        }

        use_case = FollowUserUseCase(relationship_mock_repository, user_mock_repository)
        result = use_case.execute(**relationship_data)


        self.assertEqual(result.follower_id, 1)
        self.assertEqual(result.followed_id, 2)
        self.assertEqual(user_mock_repository.called_times, 1)
        self.assertEqual(relationship_mock_repository.called_times, 2)

    def test_should_unfollow_user(self):
        relationship_mock_repository = RelationshipMockRepository()

        use_case = UnfollowUserUseCase(relationship_mock_repository)

        relationship_data = {
            "follower_id": 2,
            "followed_id": 4
        }

        result = use_case.execute(**relationship_data)

        self.assertIsNone(result)
        self.assertEqual(relationship_mock_repository.called_times, 2)