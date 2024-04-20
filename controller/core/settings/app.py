"""APPLICATION API CONFIG MODULE"""

import logging
import sys

from typing import Any, Dict, List, Tuple
from loguru import logger

from controller.core.logging import InterceptHandler
from controller.core.settings.base import BaseAppSettings

class AppSettings(BaseAppSettings):
    """ Application API configuration child class """
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Market Data Service"
    version: str = "0.0.1"

    max_connection_count: int = 10
    min_connection_count: int = 10

    api_prefix: str = "/market_data_service/v1"

    jwt_token_prefix: str = "Token"

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        """ Config class """
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """ FASTAPI config function """
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        """ Config logging function """
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])