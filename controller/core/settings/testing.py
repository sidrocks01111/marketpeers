""" Testing environment application settings module """
import logging

from pydantic import PostgresDsn, SecretStr

from controller.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    """ Test environment application settings class """
    debug: bool = True

    title: str = "Testing Environment: Provisioning Adapter"

    secret_key: SecretStr = SecretStr("test_secret")

    database_url: PostgresDsn
    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG
