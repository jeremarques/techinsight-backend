from typing import Optional
from datetime import datetime, date
from dataclasses import dataclass, field
from .user import User
import pytz

@dataclass(frozen=True)
class UserProfile():
    user: User
    name: str
    id: Optional[int] = None
    profile_photo: Optional[str] = ''
    website_url: Optional[str] = ''
    bio: Optional[str] = ''
    about: Optional[str] = ''
    date_of_birth: Optional[date] = None
    created_at: Optional[datetime] = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
        dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

        if not self.created_at:
            object.__setattr__(self, 'created_at', dt_local)

    def to_dict(self):
        return {
            'id': self.id, 
            'user_id': self.user.id,
            'profile_photo': self.profile_photo,
            'website_url': self.website_url,
            'name': self.name,
            'bio': self.bio,
            'about': self.about,
            'date_of_birth': self.date_of_birth,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }