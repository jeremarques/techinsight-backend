from datetime import datetime
import pytz
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

        except UserModel.DoesNotExist as err:
            raise NotFoundException(f'O usuário {username} não foi encontrado.')
        
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
        
