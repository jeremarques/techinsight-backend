import pytz
from uuid import uuid4,UUID
from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field
from .user_profile import UserProfile
from .post_tag import PostTag

@dataclass(frozen=True)
class Post:
    profile: UserProfile
    title: str
    slug: str
    content: str
    tag: PostTag
    id: Optional[UUID] = None
    public_id: Optional[str] = None
    created_at: Optional[datetime] = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
        dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

        if not self.public_id:
            self.set_public_id()

        if not self.created_at:
            object.__setattr__(self, 'created_at', dt_local)
    
    def set_public_id(self) -> str:
        uuid = uuid4()
        custom_id = str(uuid).replace('-', '')[:14]

        object.__setattr__(self, 'public_id', custom_id)

        return custom_id

    def to_dict(self):
        return {
            'id': self.id, 
            'public_id': self.public_id, 
            'profile': self.profile, 
            'title': self.title, 
            'slug': self.slug,
            'content': self.content, 
            'tag': self.tag, 
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }