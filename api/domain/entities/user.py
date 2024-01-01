from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field
import pytz

@dataclass(frozen=True)
class User:
    username: str
    email: str
    password: str
    id: Optional[int] = None
    full_name: Optional[str] = ''
    is_active: Optional[bool] = True
    is_staff: Optional[bool] = False
    is_superuser: Optional[bool] = False
    created_at: Optional[datetime] = field(default_factory=datetime.now)
    
    def __post_init__(self):
        dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
        dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

        if not self.created_at:
            object.__setattr__(self, 'created_at', dt_local)

    def activate(self):
        object.__setattr__(self, 'is_active', True)

    def deactivate(self):
        object.__setattr__(self, 'is_active', False)

    def to_dict(self):
        return {
            'id': self.id, 
            'username': self.username,
            'full_name': self.full_name,
            'email': self.email,
            'password': self.password,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
            'is_superuser': self.is_superuser,
            'created_at': self.created_at
        }