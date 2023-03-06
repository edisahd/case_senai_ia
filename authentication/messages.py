from core.messages import CoreMessage

class Message(CoreMessage):
    
    _invalid_credentials = 'Usuário ou senha inválido'
    _bad_renovation_token = 'Token de renovação inválido ou expirado.'

    @property
    def invalid_credentials(self) -> str:
        return self._invalid_credentials

    @property
    def bad_renovation_token(self) -> str:
        return self._bad_renovation_token