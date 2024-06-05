import pytz
from typing import Tuple
from datetime import datetime
from api.domain.entities.user import User as UserEntity
from api.models.user import User as UserModel
from api.errors import NotFoundException

class UserRepository:
    def __init__(self):
        dt_now = datetime.now(pytz.timezone('America/Fortaleza'))
        self.dt_local = dt_now.strftime('%Y-%m-%d %H:%M:%S.%f')

    def save(self, user: UserEntity) -> UserEntity:
        user_model = UserModel.from_entity(user)
        user_model.set_password(user.password)
        user_model.save()
        user_entity = user_model.to_entity()

        return user_entity
    
    def get(self, username: str) -> UserEntity:
        try:
            user_model = UserModel.objects.get(username=username)

        except UserModel.DoesNotExist:
            raise NotFoundException('Esse usuário não existe.')
        
        user_entity = user_model.to_entity()

        return user_entity
    
    def update(self, id: int, username: str, email: str, full_name: str) -> UserEntity:
        
        user_model = UserModel.objects.filter(id=id)

        user_model.update(
            username=username,
            email=email,
            full_name=full_name,
            updated_at=self.dt_local
        )
        updated_user_entity = self.get(username)

        return updated_user_entity
    
    def relations_count(self, user_id: int | None) -> Tuple[int, int]:
        user = UserModel.objects.get(id=user_id)
        followers = user.followers.count()
        following = user.following.count()

        return followers, following
    
    def following_ids(self, user_id: int | None) -> list[int]:
        user = UserModel.objects.get(id=user_id)
        following = user.following.all()

        following_ids = [item.followed_id for item in following]

        return following_ids
    
    def exists(self, *args, **kwargs) -> bool:
        user = UserModel.objects.filter(*args, **kwargs)

        if user.exists():
            return True
        else:
            return False
        
    def exists_but_not_mine(self, user_id: int, *args, **kwargs):
        user = UserModel.objects.filter(**kwargs).exclude(id=user_id)

        if user.exists():
            return True
        else:
            return False
        
