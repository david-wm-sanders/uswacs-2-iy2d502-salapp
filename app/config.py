import os
import pathlib

app_dir = pathlib.Path(__file__).parent


class ConfigurationError(Exception):
    pass

class Config:
    """Configure Flask app variables

    Security consideration: fail fast with ConfigurationError if variable not set by default
    """
    # TODO: mod to make using the object in `app.config.from_object(Config)` do the check for object is not None
    # Load app SECRET_KEY so that tools, such as CSRF protection, are usable
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ConfigurationError("No 'SECRET_KEY' set")

    # Load reCAPTCHA keys for interaction with the reCAPTCHA v2 api
    # Security consideration: reCAPTCHA helps to prevent automated systems from abusing the application
    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    if not RECAPTCHA_PUBLIC_KEY:
        raise ConfigurationError("No 'RECAPTCHA_PUBLIC_KEY' set")

    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
    if not RECAPTCHA_PRIVATE_KEY:
        raise ConfigurationError("No 'RECAPTCHA_PRIVATE_KEY' set")

    # Load DATABASE_URI from environment or use a sqlite db if environment variable is not set
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or \
                                f"sqlite:///{app_dir / 'app.db'}"

    # Disable app signalling on db changes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
