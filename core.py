# core.py
import importlib
import yaml
import os
from logger import setup_logger

class PenTestFramework:
    def __init__(self):
        self.modules = {}
        self.config = self.load_config()
        self.logger = setup_logger()

    def load_config(self):
        with open("config/settings.yaml", 'r') as f:
            return yaml.safe_load(f)

    def load_module(self, name):
        module = importlib.import_module(f'modules.{name}')
        self.modules[name] = module
        self.logger.info(f"Module {name} loaded")

    def run_module(self, name, *args, **kwargs):
        if name in self.modules:
            self.logger.info(f"Running module {name} with args: {args} and kwargs: {kwargs}")
            return self.modules[name].run(*args, **kwargs)
        else:
            self.logger.warning(f"Module {name} not found. Please load it first.")
            return None

    def list_modules(self):
        return list(self.modules.keys())

    def load_custom_modules(self):
        for filename in os.listdir("modules/"):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                self.load_module(module_name)
                self.logger.info(f"Custom module {module_name} loaded")
