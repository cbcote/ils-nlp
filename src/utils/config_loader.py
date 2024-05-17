import yaml

class ConfigLoader:
    @staticmethod
    def load_config(config_path: str) -> dict:
        """
        Load a YAML configuration file.
        
        Args:
            config_path: Local path to the YAML configuration file
        
        Returns:
            Dictionary containing the configuration
        """
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
