"""
Project related custom settings
"""
import os
import warnings

from dotenv import load_dotenv
from .django import *
from django.core.exceptions import ImproperlyConfigured


# set env variables as os env variables
load_dotenv()


# utility function to fetch env values
def get_env_value(env_variable, optional=False):
    """
    get env value (from env file)
    """
    try:
        return os.environ[env_variable]
    except KeyError:
        message = f"Env variable {env_variable} is not set!!"
        if not optional:
            raise ImproperlyConfigured(message)
        warnings.warn(message)
        return None


# DATABASES
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env_value("POSTGRES_DB"),
        "USER": get_env_value("POSTGRES_USER"),
        "PASSWORD": get_env_value("POSTGRES_PASSWORD"),
        "HOST": get_env_value("DATABASE_HOST"),
        "PORT": get_env_value("DATABASE_PORT")
    }
}

# Custom settings
DEFAULT_PAGE_SIZE = 10
CSRF_COOKIE_SECURE = False

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# STATIC
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# INSTALLED APPS
INSTALLED_APPS += [
    "apis",
    "rest_framework"
]
