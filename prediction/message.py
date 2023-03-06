from core.messages import CoreMessage

class Message(CoreMessage):
    _predict_not_found = "Prediction not found."
    _successfully_deleted = 'Prediction was successfully removed.'

    @property
    def predict_not_found(self) -> str:
        return self._predict_not_found

    @property
    def successfully_deleted(self) -> str:
        return self._successfully_deleted
