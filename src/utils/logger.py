import logging
import logging.config
import yaml

class Logger:
    @staticmethod
    def setup_logging(config_path='config/logging_config.yaml', default_level=logging.INFO):
        """
        Setup logging configuration.
        
        Args:
            config_path: Local path to the logging configuration file
            default_level: Default logging level
        
        Returns:
            None
        """
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)

    @staticmethod
    def get_logger(logger_name: str) -> logging.Logger:
        """
        Get a logger instance.
        
        Args:
            logger_name: Name of the logger
        
        Returns:
            Logger instance
        """
        return logging.getLogger(logger_name)
