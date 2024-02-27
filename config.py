import yaml

class ConfigLoader:
    """Loads configuration from a local YAML file."""
    
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        """Loads and returns the configuration from the YAML file."""
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)