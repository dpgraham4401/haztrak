"""Settings for prod."""

import os

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
        "ENGINE": os.environ.get("HT_DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("HT_DB_NAME"),
        "USER": os.environ.get("HT_DB_USER"),
        "PASSWORD": os.environ.get("HT_DB_PASSWORD"),
        "HOST": os.environ.get("HT_DB_HOST"),
        "PORT": os.environ.get("HT_DB_PORT", "5432"),
    },
}
