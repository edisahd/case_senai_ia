class CoreMessage:
    _invalid_input = 'Formato de entrada inválido.'
    _server_error = 'Erro interno no servidor.'
    _unauthorized = 'Usuário sem permissão!'
    _limit_error = 'Limite deve ser um valor positivo'
    _offset_error = 'Deslocamento deve ser um valor positivo'

    @property
    def invalid_input(self) -> str:
        return self._invalid_input

    @property
    def server_error(self) -> str:
        return self._server_error

    @property
    def unauthorized(self) -> str:
        return self._unauthorized

    @property
    def limit_error(self) -> str:
        return self._limit_error
    
    @property
    def offset_error(self) -> str:
        return self._offset_error