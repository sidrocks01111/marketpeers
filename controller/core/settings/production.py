""" Production environment application settings module """
from controller.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    """ Production environment application settings class """
    class Config(AppSettings.Config):
        """ Application config class """
        env_file = "prod.env"
