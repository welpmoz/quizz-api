from fastapi import HTTPException, status

class Missing(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg


class Format(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg


def handle_common_errors(exc: Exception):
    if isinstance(exc, Format):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=exc.msg,
        )
    
    if isinstance(exc, Missing):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.msg,
        )
    
    raise exc
