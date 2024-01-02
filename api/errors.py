
class NotFoundException(Exception):
    """Levanta uma exceção quando um recurso solicitado não é encontrado."""

    def __init__(self, message: str = "Recurso não encontrado"):
        self.message = message
        super().__init__(self.message)

