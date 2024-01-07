import pytz
from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field

from .user_profile import UserProfile
from .post import Post

@dataclass(frozen=True)
class PostLike:
    profile_id: UserProfile
    post_id: Post
    id: Optional[int] = None
    created_at: Optional[datetime] = field(default_factory=datetime.now)
    
    def __post_init__(self):
        dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
        dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

        if not self.created_at:
            object.__setattr__(self, 'created_at', dt_local)

    def to_dict(self):
        return {
            'id': self.id,
            'profile_id': self.profile_id,
            'post_id': self.post_id, 
            'created_at': self.created_at,
        }