from api.domain.entities.user import User as UserEntity
from api.infrastructure.adapters.repositories.user import UserRepository
from api.domain.errors import NotFoundException

class CreateUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.user_repository = repository

    def execute(self, username: str, password: str, email: str, full_name: str) -> UserEntity:
        user = UserEntity(
            username=username,
            password=password,
            email=email,
            full_name=full_name,
        )

        user_entity = self.user_repository.save(user)

        return user_entity


class GetUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.user_repository = repository

    def execute(self, username: str) -> UserEntity:
        try:
            users_list = self.user_repository.get(username)

        except NotFoundException as err:
            raise err

        return users_list


class UpdateUserUseCase:
    def __init__(self, repository: UserRepository) -> None: 
        self.user_repository = repository

    def execute(self, id: int, username: str, email: str, full_name: str) -> UserEntity:
        try:
            updated_user = self.user_repository.update(id, username, email, full_name)
        
        except NotFoundException as err:
            raise err
        
        return updated_user