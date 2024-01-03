from api.domain.entities.user import User as UserEntity
from api.infrastructure.adapters.repositories.user import UserRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.domain.use_cases.user_profile import CreateUserProfileUseCase
from api.errors import NotFoundException

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository, user_profile_repository: UserProfileRepository) -> None:
        self.user_repository = user_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, username: str, password: str, email: str, full_name: str) -> UserEntity:
        user = UserEntity(
            username=username,
            password=password,
            email=email,
            full_name=full_name,
        )

        user_entity = self.user_repository.save(user)

        create_user_profile_use_case = CreateUserProfileUseCase(self.user_profile_repository)
        created_user_profile = create_user_profile_use_case.execute(user_id=user_entity.id, name=user_entity.full_name)

        return user_entity


class GetUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.user_repository = repository

    def execute(self, username: str) -> UserEntity:
        try:
            user = self.user_repository.get(username)

        except NotFoundException as err:
            raise err

        return user


class UpdateUserUseCase:
    def __init__(self, repository: UserRepository) -> None: 
        self.user_repository = repository

    def execute(self, id: int, username: str, email: str, full_name: str) -> UserEntity:
        try:
            updated_user = self.user_repository.update(id, username, email, full_name)
        
        except NotFoundException as err:
            raise err
        
        return updated_user