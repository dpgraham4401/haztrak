"""Settings for development environment."""

from .base import *  # noqa: F403, S105, RUF100
from .base import env

# General
with env.prefixed("TRAK_"):
    SIGNING_KEY = env.str(
        "SIGNING_KEY", "0dd3f4e68730bedfb07e6bc2e8f00a56c4db2d4a4b37e64ac0a83b8c97ec55dd"
    )
    ALLOWED_HOSTS = env.list("HOST", ["localhost", "*"])
    SECRET_KEY = env.str(
        "SECRET_KEY", "django-insecure-%btjqoun@6ps$e@8bw$48s+!x1e4aiz&5p2nrf6cmiw4)jsx5d"
    )
    DEBUG = env.bool("DEBUG", True)
    CORS_ORIGIN_WHITELIST = env.list("CORS_DOMAIN", ["http://localhost"])

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
]

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": env.str("TRAK_DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": env.str("TRAK_DB_NAME", "db.sqlite3"),
        "USER": env.str("TRAK_DB_USER", "admin"),
        "PASSWORD": env.str("TRAK_DB_PASSWORD", "password"),
        "HOST": env.str("TRAK_DB_HOST", "localhost"),
        "PORT": env.str("TRAK_DB_PORT", "5432"),
    },
}
FIXTURE_DIRS = ["fixtures"]
