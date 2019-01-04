import os

class ConfigurationError(Exception):
    pass

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ConfigurationError("No 'SECRET_KEY' set for environment")
