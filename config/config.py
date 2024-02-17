import yaml
import json

"""
The Config class represents a configuration object that loads and manages a YAML configuration file.

Attributes:
    config (dict): A dictionary that stores the loaded configuration data.

Methods:
    __init__(self, config_file):
        Initializes a Config object by loading the configuration data from the specified file.

    load_config(self, config_file):
        Loads the configuration data from the specified file and returns it as a dictionary.

    get_library_config(self, library_name):
        Retrieves the configuration data for the specified library name.

    is_library_active(self, library_name):
        Checks if the specified library is active based on its configuration.

    get_library_index(self, library_name):
        Retrieves the index value for the specified library based on its configuration.

"""

class Config:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_library_config(self, library_name):
        if library_name in self.config:
            return self.config[library_name]
        else:
            return None

    def is_library_active(self, library_name):
        library_config = self.get_library_config(library_name)
        if library_config:
            return library_config.get('active', False)
        else:
            return False

    def get_library_index(self, library_name):
        library_config = self.get_library_config(library_name)
        if library_config:
            return library_config.get('index', '')
        else:
            return None

if __name__ == "__main__":
    config = Config('./mlops/config.yaml')
    print(f"{library_name} active status:", config.is_library_active(library_name))
    print(f"{library_name} index:", config.get_library_index(library_name))
