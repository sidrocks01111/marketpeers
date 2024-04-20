""" HTTP error module """
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """
    Function to handle HTTP errors
    :@param _: HTTP request
    :@param exc: HTTP exception
    """
    return JSONResponse({'error': [exc.detail]}, status_code=exc.status_code)