from api.domain.entities.user import User as UserEntity
from api.models.user import User as UserModel

class UserRepository:
    def save(self, user: UserEntity) -> UserEntity:
        user_model = UserModel.from_entity(user)
        user_model.set_password(user.password)
        user_model.save()
        user_entity = user_model.to_entity()

        return user_entity
    
    def get(self, username: str) -> UserEntity:
        user_model = UserModel.objects.get(username=username)
        user_entity = user_model.to_entity()

        return user_entity
    
    def update(self, id: int, username: str, email: str, full_name: str) -> UserEntity:
        user_model = UserModel.objects.filter(id=id)

        user_model.update(
            username=username,
            email=email,
            full_name=full_name
        )
        updated_user_entity = self.get(username)

        return updated_user_entity

    def exists_by_id(self, user_id: int) -> bool:
        user = UserModel.objects.filter(id=user_id)

        if user.exists():
            return True
        else:
            return False
        
    def exists_by_username(self, username: int) -> bool:
        user = UserModel.objects.filter(username=username)

        if user.exists():
            return True
        else:
            return False
