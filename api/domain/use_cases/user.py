from api.domain.entities.user import User as UserEntity
from api.infrastructure.adapters.repositories.user import UserRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.domain.use_cases.user_profile import CreateUserProfileUseCase
from api.domain.dtos.user_dto import UserDTO
from api.errors import NotFoundException, AlreadyExistsException, UsernameAlreadyExistsException, EmailAlreadyExistsException


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository, user_profile_repository: UserProfileRepository) -> None:
        self.user_repository = user_repository
        self.user_profile_repository = user_profile_repository

    def execute(self, username: str, password: str, email: str, full_name: str) -> UserDTO:
        exists_username = self.user_repository.exists(username=username)
        exists_email = self.user_repository.exists(email=email)
        
        if exists_username and exists_email:
            raise AlreadyExistsException(f'Esse nome de usuário e e-mail já existem.')
        
        elif exists_username:
            raise UsernameAlreadyExistsException(f'Esse nome de usuário já existe.')
        
        elif exists_email:
            raise EmailAlreadyExistsException(f'Esse e-mail já existe.')

        user = UserEntity(
            username=username,
            password=password,
            email=email,
            full_name=full_name,
        )

        try:
            user_entity = self.user_repository.save(user)
            create_user_profile_use_case = CreateUserProfileUseCase(self.user_profile_repository)
            created_user_profile = create_user_profile_use_case.execute(user=user_entity, name=user_entity.full_name)

        except Exception:
            raise Exception('Ocorreu um erro ao registrar o usuário.')

        user = UserDTO(user_entity, 0, 0)

        return user


class GetUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, username: str, user_id: int | None) -> UserDTO:
        try:
            user_entity = self.user_repository.get(username)
            followers, following = self.user_repository.relations_count(user_entity.id)
            if user_id != None:
                following_ids = self.user_repository.following_ids(user_id)
            else:
                following_ids = []

        except NotFoundException as err:
            raise err
        
        except Exception:
            raise Exception('Ocorreu um erro ao buscar o usuário.')

        user = UserDTO(user_entity, followers, following, user_entity.id in following_ids)
        return user


class UpdateUserUseCase:
    def __init__(self, repository: UserRepository) -> None: 
        self.user_repository = repository

    def execute(self, id: int, username: str, email: str, full_name: str) -> UserDTO:
        if not self.user_repository.exists(id=id):
            raise NotFoundException('Esse usuário não existe.')
        
        exists_username = self.user_repository.exists_but_not_mine(id, username=username)
        exists_email = self.user_repository.exists_but_not_mine(id, email=email)
        
        if exists_username and exists_email:
            raise AlreadyExistsException(f'Esse nome de usuário e e-mail já existem.')
        
        elif exists_username:
            raise UsernameAlreadyExistsException(f'Esse nome de usuário já existe.')
        
        elif exists_email:
            raise EmailAlreadyExistsException(f'Esse e-mail já existe.')
        
        try:
            updated_user_entity = self.user_repository.update(id, username, email, full_name)
            followers, following = self.user_repository.relations_count(updated_user_entity.id)
        
        except Exception as err:
            print(err)
            raise Exception('Ocorreu um erro ao atualizar o usuário.')
        

        updated_user = UserDTO(updated_user_entity, followers, following)

        return updated_user