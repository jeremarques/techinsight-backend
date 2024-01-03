from api.domain.entities.user import User as UserEntity
from api.models.user import User as UserModel
from api.errors import NotFoundException

class UserRepository:
    def save(self, user: UserEntity) -> UserEntity:
        user_model = UserModel.from_entity(user)
        user_model.set_password(user.password)
        user_model.save()
        user_entity = user_model.to_entity()

        return user_entity
    
    def get(self, username: str) -> UserEntity:
        try:
            user_model = UserModel.objects.get(username=username)
            user_entity = user_model.to_entity()

        except UserModel.DoesNotExist as err:
            raise NotFoundException(f'O usuário {username} não foi encontrado.')

        return user_entity
    
    def update(self, id: int, username: str, email: str, full_name: str) -> UserEntity:
        user_model = UserModel.objects.filter(id=id)

        if not user_model.exists():
            raise NotFoundException(f'O usuário com id {id} não foi encontrado.')

        user_model.update(
            username=username,
            email=email,
            full_name=full_name
        )
        updated_user_entity = self.get(username)

        return updated_user_entity
