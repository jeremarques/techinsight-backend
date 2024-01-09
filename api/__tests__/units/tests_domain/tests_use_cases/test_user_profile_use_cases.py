import unittest
from datetime import datetime
from api.domain.entities.user_profile import UserProfile
from api.domain.entities.user import User
from api.domain.use_cases.user_profile import CreateUserProfileUseCase, GetUserProfileUseCase, UpdateUserProfileUseCase

class UserProfileMockRepository:
    called_times = 0
    
    def save(self, user_profile: UserProfile):
        self.called_times += 1
        
        return UserProfile(
            user=user_profile.user,
            name=user_profile.name
        )
    
    def get(self, *args, **kwargs):
        self.called_times += 1

        user = {
            'id': 1,
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        return UserProfile(user=User(**user), name=user.get('full_name'))
    
    def update(self, user_id, name, profile_photo, website_url, bio, about, date_of_birth):
        self.called_times += 1

        user = {
            'id': user_id,
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        return UserProfile(User(**user), name=name, profile_photo=profile_photo, website_url=website_url, bio=bio, about=about, date_of_birth=date_of_birth)
    
    def exists(self, *args, **kwargs):
        self.called_times += 1

        return True


class UserMockRepository:
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
    
    def relations_count(self, id: int, *args, **kwargs):
        self.called_times += 1
        
        return 2, 8


class TestUserProfileUseCases(unittest.TestCase):
    def test_create_user_profile(self):
        user_profile_mock_repository = UserProfileMockRepository()

        user = {
            'username': 'jeremias',
            'email': 'jeremias@gmail.com',
            'password': 'password123',
            'full_name': 'Jeremias Marques'
        }

        user_profile_data = {
            'user': User(**user),
            'name': 'Jeremias Marques'
        }

        use_case = CreateUserProfileUseCase(user_profile_mock_repository)
        result = use_case.execute(**user_profile_data)


        self.assertEqual(result.name, 'Jeremias Marques')
        self.assertEqual(result.user.username, 'jeremias')
        self.assertEqual(result.user.email, 'jeremias@gmail.com')
        self.assertEqual(result.user.password, 'password123')
        self.assertEqual(result.user.full_name, result.name)
        self.assertEqual(user_profile_mock_repository.called_times, 1)

    def test_should_return_user_profile(self):
        user_profile_mock_repository = UserProfileMockRepository()
        user_mock_repository = UserMockRepository()

        use_case = GetUserProfileUseCase(user_profile_mock_repository, user_mock_repository)

        result = use_case.execute('jeremias', None)

        self.assertEqual(result.user.id, 1)
        self.assertEqual(result.name, 'Jeremias Marques')
        self.assertEqual(result.user.username, 'jeremias')
        self.assertEqual(result.user.email, 'jeremias@gmail.com')
        self.assertEqual(result.user.full_name, result.name)
        self.assertEqual(result.user.followers, 2)
        self.assertEqual(result.user.following, 8)
        self.assertEqual(result.user.is_follower, False)
        self.assertEqual(user_profile_mock_repository.called_times, 1)
        self.assertEqual(user_mock_repository.called_times, 2)

    def test_should_update_user_profile(self):
        user_profile_mock_repository = UserProfileMockRepository()
        user_mock_repository = UserMockRepository()

        use_case = UpdateUserProfileUseCase(user_profile_mock_repository, user_mock_repository)

        result = use_case.execute(1, 'Jeremias', 'profile_photo_url', 'website_url', 'My Bio', 'About me', '2007-11-03')

        self.assertEqual(result.user.id, 1)
        self.assertEqual(result.user.username, 'jeremias')
        self.assertEqual(result.user.email, 'jeremias@gmail.com')
        self.assertEqual(result.user.full_name, 'Jeremias Marques')
        self.assertEqual(result.user.followers, 2)
        self.assertEqual(result.user.following, 8)
        self.assertEqual(result.user.is_follower, False)
        self.assertEqual(result.name, 'Jeremias')
        self.assertEqual(result.profile_photo, 'profile_photo_url')
        self.assertEqual(result.website_url, 'website_url')
        self.assertEqual(result.bio, 'My Bio')
        self.assertEqual(result.about, 'About me')
        self.assertEqual(result.date_of_birth, '2007-11-03')
        self.assertEqual(user_profile_mock_repository.called_times, 2)
        self.assertEqual(user_mock_repository.called_times, 1)