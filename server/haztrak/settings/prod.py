"""Settings for prod."""

from .base import *  # noqa: F403
from .base import SIMPLE_JWT, env

# General
DEBUG = False
with env.prefixed("TRAK_"):
    SECRET_KEY = env.str("SECRET_KEY")
    ALLOWED_HOSTS: list[str] = env.list("HOSTS")
    CORS_ORIGIN_WHITELIST: list[str] = env.list("CORS_DOMAIN")
    SIGNING_KEY = env.str("SIGNING_KEY")

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


SIMPLE_JWT = {
    **SIMPLE_JWT,
    "SIGNING_KEY": SIGNING_KEY,
}
