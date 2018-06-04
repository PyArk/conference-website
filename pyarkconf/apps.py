from django.apps import AppConfig as BaseAppConfig
from importlib import import_module


class AppConfig(BaseAppConfig):

    name = "pyarkconf"

    def ready(self):
        import_module("pyarkconf.receivers")
