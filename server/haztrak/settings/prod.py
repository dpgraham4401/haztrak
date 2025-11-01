"""Settings for prod."""

from django.conf.global_settings import ALLOWED_HOSTS

from .base import *  # noqa: F403
from .base import env

# General
DEBUG = False
ALLOWED_HOSTS = env.list("TRAK_HOSTS")  # noqa
CORS_ORIGIN_WHITELIST = env.list("TRAK_CORS_DOMAIN")

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": env.str("TRAK_DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": env.str("TRAK_DB_NAME"),
        "USER": env.str("TRAK_DB_USER"),
        "PASSWORD": env.str("TRAK_DB_PASSWORD"),
        "HOST": env.str("TRAK_DB_HOST"),
        "PORT": env.str("TRAK_DB_PORT", "5432"),
    },
}
