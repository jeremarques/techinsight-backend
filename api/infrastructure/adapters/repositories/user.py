from api.domain.entities.user import User as UserEntity
from api.models import User as UserModel

class UserRepository:
    def save(self, user: UserEntity) -> UserEntity:
        user_model = UserModel.from_entity(user)
        user_model.save()
        user_entity = user_model.to_entity()

        return user_entity
    
    def list_all(self) -> list[UserEntity]:
        users_models = UserModel.objects.all()
        users_entities = [user_model.to_entity() for user_model in users_models]

        return users_entities