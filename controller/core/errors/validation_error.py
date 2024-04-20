" HTTP request validation module "

from typing import Union

from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http422_error_handler(
        _: Request, exc: Union[RequestValidationError,
                               ValidationError]) -> JSONResponse:
    """
    Un-processable entity function
    @param _: API request
    @param exc: Request or validation exception
    """
    return JSONResponse({"errors": exc.errors()},
                        status_code=HTTP_422_UNPROCESSABLE_ENTITY)
