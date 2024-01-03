
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
