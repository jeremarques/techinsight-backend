from datetime import datetime
from dataclasses import dataclass, field

@dataclass(frozen=True)
class User:
    id = int
    username = str
    full_name = str
    email = str
    password = str
    is_active = bool
    created_at = field(default_factory=datetime.now())
    
    def __post_init__(self):
        if not self.created_at:
            object.__setattr__(self, 'created_at', datetime.now())

    def to_dict(self):
        return {
            'id': self.id, 
            'username': self.username, 
            'full_name': self.full_name,
            'email': self.email,
            'full_name': self.full_name,
            'is_active': self.is_active,
            'created_at': self.created_at
        }