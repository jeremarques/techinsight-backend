from django.db import IntegrityError


class ForbiddenException(Exception):
    """Raises an exception when a access to the resource is prohibited."""

    def __init__(self, message: str = "Acesso negado"):
        self.message = message
        super().__init__(self.message)


class NotFoundException(Exception):
    """Raises an exception when a requested resource is not found."""

    def __init__(self, message: str = "Recurso não encontrado"):
        self.message = message
        super().__init__(self.message)


class AlreadyExistsException(Exception):
    """Raises an exception when trying to create an existing resource"""

    def __init__(self, message: str = "Recurso já existente"):
        self.message = message
        super().__init__(self.message)


class UsernameAlreadyExistsException(Exception):
    """Raises an exception when trying to create an resource with an existing username"""

    def __init__(self, message: str = "O nome de usuário já existe"):
        self.message = message
        super().__init__(self.message)


class EmailAlreadyExistsException(Exception):
    """Raises an exception when trying to create an resource with an existing e-mail"""

    def __init__(self, message: str = "O e-mail já existe"):
        self.message = message
        super().__init__(self.message)