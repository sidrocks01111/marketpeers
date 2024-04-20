"""BASE ENV CONFIG MODULE"""
from enum import Enum
from pydantic_settings import BaseSettings

class AppEnvTypes(Enum):
    """ Application environment class"""
    prod: str = "prod"
    dev: str = "dev"
    testing: str = "testing"

class BaseAppSettings(BaseSettings):
    """ Base application environment config class """
    app_env: AppEnvTypes = AppEnvTypes.prod

    class Config:
        """ Application environment config class """
        env_file = ".env"
