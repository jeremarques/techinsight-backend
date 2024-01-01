from datetime import datetime
import pytz


class User:
    def __init__(self, username, email, password, created_at, full_name = '', is_active = True, is_staff = False, id = None):
        self.id = id
        self.username = username
        self.full_name = full_name
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_staff = is_staff
        self.created_at = created_at

    
    def check_created_at(self):
        dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

        if not self.created_at:
            self.created_at = self.dt_local

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def to_dict(self):
        return {
            'id': self.id, 
            'username': self.username,
            'full_name': self.full_name,
            'email': self.email,
            'password': self.password,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
            'created_at': self.created_at
        }