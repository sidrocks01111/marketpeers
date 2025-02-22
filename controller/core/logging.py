""" Application logger module """
import logging
from types import FrameType
from typing import cast

from loguru import logger


class InterceptHandler(logging.Handler):
    """ Intercept class """
    def emit(self, record: logging.LogRecord) -> None:
        """
        Function to get corresponding Loguru level if it exists
        @param record: Log record
        """
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )
