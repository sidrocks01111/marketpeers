""" Development environment application settings module """
import logging

from controller.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    """ Development environment application settings class """
    debug: bool = True

    title: str = "Dev Environment: Provisioning Adapter"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        """ Environment config class """
        env_file = ".env"
