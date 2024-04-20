""" Provisioning adapter API settings module """
from functools import lru_cache
from typing import Dict, Type

from controller.core.settings.app import AppSettings
from controller.core.settings.base import AppEnvTypes, BaseAppSettings
from controller.core.settings.development import DevAppSettings
from controller.core.settings.production import ProdAppSettings
from controller.core.settings.testing import TestAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.testing: TestAppSettings,
}


# @lru_cache
def get_app_settings() -> AppSettings:
    """
    Function to load environment details
    """
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
