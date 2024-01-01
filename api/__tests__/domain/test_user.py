import unittest
from api.domain.entities.user import User

class TestUserDomainUnit(unittest.TestCase):
    def test_constructor(self):
        user = User('jeremias', 'email@email.com', 'password123')
        self.assertIsNone(user.id)
        self.assertEqual(user.username, 'jeremias')
        self.assertEqual(user.email, 'email@email.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.full_name, '')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_deactivate_and_activate(self):
        user = User('jeremias', 'email@email.com', 'password123')
        self.assertTrue(user.is_active)
        user.deactivate()
        self.assertFalse(user.is_active)
        user.activate()
        self.assertTrue(user.is_active)

