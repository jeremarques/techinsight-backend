from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field
import pytz

@dataclass(frozen=True)
class PostTag:
    name: str
    slug: str
    created_at: Optional[datetime] = field(default_factory=datetime.now)
    
    def __post_init__(self):
        dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
        dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

        if not self.created_at:
            object.__setattr__(self, 'created_at', dt_local)

    def to_dict(self):
        return {
            'name': self.name, 
            'slug': self.slug,
            'created_at': self.created_at
        }