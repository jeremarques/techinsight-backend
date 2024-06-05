from uuid import UUID
import pytz
from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field

from .user_profile import UserProfile

@dataclass(frozen=True)
class PostComment:
    profile: UserProfile
    content: str
    post_id: Optional[UUID] = None
    id: Optional[int] = None
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
            'profile_id': self.profile,
            'post_id': self.post_id,
            'content': self.content,
            'created_at': self.created_at
        }