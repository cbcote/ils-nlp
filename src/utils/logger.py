import logging
import logging.config
import yaml

class Logger:
    @staticmethod
    def setup_logging(config_path='config/logging_config.yaml', default_level=logging.INFO):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)

    @staticmethod
    def get_logger(logger_name):
        return logging.getLogger(logger_name)
