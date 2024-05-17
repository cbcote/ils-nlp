# tests/test_config_loader.py
import unittest
from src.utils.config_loader import ConfigLoader

class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        config = ConfigLoader.load_config('config/config.yaml')
        self.assertIsNotNone(config)
        self.assertIn('preprocessing', config)

if __name__ == '__main__':
    unittest.main()
