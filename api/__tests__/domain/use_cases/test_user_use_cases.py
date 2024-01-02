import unittest

from api.domain.entities.user import User
from api.domain.use_cases.user import CreateUserUseCase

class MockRepository:
    called_times = 0

    def save(self, user: User):
        self.called_times += 1
        
        return User(
            id=user.id,
            username=user.username,
            password=user.password,
            email=user.email,
            full_name=user.full_name,
            is_staff=user.is_staff,
            is_superuser=user.is_superuser,
            is_active=user.is_active,
            created_at=user.created_at
        )


class TestUserUseCases(unittest.TestCase):
    def test_should_create_normal_user(self):
        mock_repositorie = MockRepository()
        user = {
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        use_case = CreateUserUseCase(mock_repositorie)
        result = use_case.execute(**user)

        self.assertEqual(result.username, 'jeremias')
        self.assertEqual(result.email, 'jeremias@gmail.com')
        self.assertEqual(result.password, 'password123')
        self.assertEqual(result.full_name, 'Jeremias Marques')
        self.assertEqual(result.is_staff, False)
        self.assertEqual(result.is_superuser, False)
        self.assertEqual(result.is_active, True)
        self.assertEqual(mock_repositorie.called_times, 1)
        