import os

class ConfigurationError(Exception):
    pass

class Config:
    """Configure Flask app variables

    Security consideration: fail fast with ConfigurationError if variable not set
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ConfigurationError("No 'SECRET_KEY' set")

    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    if not RECAPTCHA_PUBLIC_KEY:
        raise ConfigurationError("No 'RECAPTCHA_PUBLIC_KEY' set")

    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
    if not RECAPTCHA_PRIVATE_KEY:
        raise ConfigurationError("No 'RECAPTCHA_PRIVATE_KEY' set")
