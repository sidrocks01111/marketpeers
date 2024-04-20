"""REST API MAIN CONTROLLER"""
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from api_client.config.constants import load_dotenv
from api_client.db_connector import init_mongodb
from controller.api.routers.api import router as api_router
from controller.core.errors.http_error import http_error_handler
from controller.core.errors.validation_error import http422_error_handler
from controller.core.config import get_app_settings


def get_application():
    """Function to set application setting"""

    # settings = get_app_settings()

    # settings.configure_logging()

    application = FastAPI(
        debug=False,
        docs_url="/docs",
        openapi_prefix="",
        openapi_url="/openapi.json",
        redoc_url="/redoc",
        title="Market Data Service",
        version="0.0.1")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(
        RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix="/marketpeers/v1")

    return application


app = get_application()

@app.on_event("startup")
async def startup():
    try:
        await init_mongodb()
    except:
        print("\t*****database is not initialized*****")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8012, reload=True)
