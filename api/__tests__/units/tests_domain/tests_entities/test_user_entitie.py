import unittest
from datetime import datetime

from api.domain.entities.user import User

class TestUserEntitieUnit(unittest.TestCase):

    def test_constructor(self):
        user = User('jeremias', 'email@email.com', 'password123', created_at=datetime(2024, 1, 1, 15, 32, 46, 428775))
        self.assertIsNone(user.id)
        self.assertEqual(user.username, 'jeremias')
        self.assertEqual(user.email, 'email@email.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.full_name, '')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.created_at, datetime(2024, 1, 1, 15, 32, 46, 428775))
        self.assertIsNone(user.updated_at)

    def test_deactivate_and_activate(self):
        user = User('jeremias', 'email@email.com', 'password123')
        self.assertTrue(user.is_active)
        user.deactivate()
        self.assertFalse(user.is_active)
        user.activate()
        self.assertTrue(user.is_active)

