from fastapi import Response
from fastapi import status as statuscode

__all__ = ("OK_200",)


OK_200 = Response(
    content="OK",
    media_type="text/plain",
    status_code=statuscode.HTTP_200_OK
)
