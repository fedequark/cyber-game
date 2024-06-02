import importlib
import os

class PluginManager:
    def __init__(self, plugin_folder):
        self.plugin_folder = plugin_folder
        self.plugins = []

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module = importlib.import_module(f'plugins.{module_name}')
                self.plugins.append(module)

    def get_plugins(self):
        return self.plugins