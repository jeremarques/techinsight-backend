import unittest
from datetime import datetime

from api.domain.entities.user_profile import UserProfile

class TestProfileDomainUnit(unittest.TestCase):

    def test_constructor(self):
        profile = UserProfile(
            1,
            'Jeremias Marques',
            1,
            'profile_image',
            'mywebsite.com',
            'my bio',
            'about',
            created_at=datetime(2024, 1, 1, 15, 32, 46, 428775)
        )
        self.assertEqual(profile.id, 1)
        self.assertEqual(profile.user_id, 1)
        self.assertEqual(profile.name, 'Jeremias Marques')
        self.assertEqual(profile.profile_photo, 'profile_image')
        self.assertEqual(profile.website_url, 'mywebsite.com')
        self.assertEqual(profile.bio, 'my bio')
        self.assertEqual(profile.about, 'about')
        self.assertEqual(profile.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))

