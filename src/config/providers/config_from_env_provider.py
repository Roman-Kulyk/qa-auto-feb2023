import os
from src.config.providers.base_config import BaseConfigKeyProvider


#BaseConfigEnvProvider usage is optional
class ConfigFromEnvProvider(BaseConfigKeyProvider):
    """
    Allows configuration through the env variables.
    """
    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        return os.environ.get(key)