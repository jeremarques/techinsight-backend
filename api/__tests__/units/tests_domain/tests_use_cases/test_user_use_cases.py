import unittest
from datetime import datetime

from api.domain.entities.user import User
from api.domain.entities.user_profile import UserProfile
from api.domain.use_cases.user import CreateUserUseCase, GetUserUseCase, UpdateUserUseCase

class MockRepository:
    called_times = 0

    def get(self, username: str):
        self.called_times += 1

        return User(
            id=1,
            username=username,
            password='password123',
            email='email@email.com',
            full_name='Jeremias Marques',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )

    
    def save(self, user: User):
        self.called_times += 1
        
        return User(
            id=1,
            username=user.username,
            password=user.password,
            email=user.email,
            full_name=user.full_name,
            is_staff=user.is_staff,
            is_superuser=user.is_superuser,
            is_active=user.is_active,
            created_at=user.created_at
        )
    
    def update(self, id: int, username: str, email: str, full_name: str):
        self.called_times += 1

        return User(
            id=id,
            username=username,
            password='password123',
            email=email,
            full_name=full_name,
            is_staff=False,
            is_superuser=False,
            is_active=True,
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )

    def relations_count(self, id: int, *args, **kwargs):
        self.called_times += 1
        
        return 2, 8

    def exists(self, *args, **kwargs):
        self.called_times += 1

        if kwargs.get('username') == 'jeremias':
            return False
        
        if kwargs.get('email') == 'jeremias@gmail.com':
            return False
        
        return True
    
    def exists_but_not_mine(self, id: int, *args, **kwargs):
        self.called_times += 1
        
        return False
    

class MockRepositoryProfile:
    called_times = 0
    
    def save(self, user_profile: UserProfile):
        self.called_times += 1
        
        return UserProfile(
            user=user_profile.user,
            name=user_profile.name
        )
    

class TestUserUseCases(unittest.TestCase):
    def test_should_create_normal_user(self):
        mock_repository = MockRepository()
        mock_repository_profile = MockRepositoryProfile()

        user = {
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        use_case = CreateUserUseCase(mock_repository, mock_repository_profile)
        result = use_case.execute(**user)

        self.assertEqual(result.username, 'jeremias')
        self.assertEqual(result.email, 'jeremias@gmail.com')
        self.assertEqual(result.full_name, 'Jeremias Marques')
        self.assertEqual(result.followers, 0)
        self.assertEqual(result.following, 0)
        self.assertEqual(result.is_follower, False)
        self.assertEqual(mock_repository.called_times, 3)

    def test_should_return_user(self):
        mock_repository = MockRepository()

        use_case = GetUserUseCase(mock_repository)
        result = use_case.execute('jeremias', None)

        self.assertEqual(result.username, 'jeremias')
        self.assertEqual(result.email, 'email@email.com')
        self.assertEqual(result.full_name, 'Jeremias Marques')
        self.assertEqual(result.followers, 2)
        self.assertEqual(result.following, 8)
        self.assertEqual(result.is_follower, False)
        self.assertEqual(result.is_active, True)
        self.assertEqual(result.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))
        self.assertEqual(mock_repository.called_times, 2)

    def test_should_return_updated_user(self):
        mock_repository = MockRepository()

        use_case = UpdateUserUseCase(mock_repository)
        result = use_case.execute(1, 'jeremias', 'email@email.com', 'Jeremias Marques')

        self.assertEqual(result.id, 1)
        self.assertEqual(result.username, 'jeremias')
        self.assertEqual(result.email, 'email@email.com')
        self.assertEqual(result.full_name, 'Jeremias Marques')
        self.assertEqual(result.is_active, True)
        self.assertEqual(result.followers, 2)
        self.assertEqual(result.following, 8)
        self.assertEqual(result.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))
        self.assertEqual(mock_repository.called_times, 5)