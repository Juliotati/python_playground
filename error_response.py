from fastapi import HTTPException


class ErrorResponse(HTTPException):
    status_code: int
    message: str
    headers: {}

    def __init__(self, status_code: int, message: str, headers: {} = None):
        self.status_code = status_code
        self.message = message
        super().__init__(status_code=status_code, detail=message, headers=headers)

    @staticmethod
    def not_found(requested_item_id):
        raise ErrorResponse(
            404,
            f'Found no item with with the given id {requested_item_id}',
            headers={"X-Error": "ErrorResponse.not_found was raised"},
        )
