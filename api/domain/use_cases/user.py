from api.domain.entities.user import User
from api.infrastructure.adapters.repositories.user import UserRepository

class CreateUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.user_repository = repository

    def execute(self, username: str, password: str, email: str, full_name: str) -> User:
        user = User(
            username=username,
            password=password,
            email=email,
            full_name=full_name,
        )

        user_entity = self.user_repository.save(user)

        return user_entity


class ListUsersUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.user_repository = repository

    def execute(self) -> list[User]:
        users_list = self.user_repository.list_all()

        return users_list
