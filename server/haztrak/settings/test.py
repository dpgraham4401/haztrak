"""Settings for test environment."""

from pathlib import Path

from .base import *  # noqa: F403
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
    DEBUG = env.bool("DEBUG", False)
    # CORS_ORIGIN_WHITELIST = env.list("CORS_DOMAIN", ["http://localhost"])
    CORS_ORIGIN_WHITELIST = env.list("CORS_DOMAIN", "http://*")

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
]

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": env.str("TRAK_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": env.str("TRAK_DB_NAME", str(Path(BASE_DIR) / "db.sqlite3")),  # noqa: F405
        "USER": env.str("TRAK_DB_USER", "user"),
        "PASSWORD": env.str("TRAK_DB_PASSWORD", "password"),
        "HOST": env.str("TRAK_DB_HOST", "localhost"),
        "PORT": env.str("TRAK_DB_PORT", "5432"),
        "TEST": {
            "NAME": "test_db",
        },
    },
}
FIXTURE_DIRS = ["fixtures"]
