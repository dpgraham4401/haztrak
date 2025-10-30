"""Settings for test environment."""

import os
from pathlib import Path

from .base import *  # noqa: F403

# General
SECRET_KEY = "django-insecure-%btjqoun@6ps$e@8bw$48s+!x1e4aiz&5p2nrf6cmiw4)jsx5d"
DEBUG = True
CORS_ORIGIN_WHITELIST = [os.getenv("HT_CORS_DOMAIN", "http://*")]
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
]

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("HT_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("HT_DB_NAME", Path(BASE_DIR) / "db.sqlite3"),  # noqa: F405
        "USER": os.environ.get("HT_DB_USER", "user"),
        "PASSWORD": os.environ.get("HT_DB_PASSWORD", "password"),
        "HOST": os.environ.get("HT_DB_HOST", "localhost"),
        "PORT": os.environ.get("HT_DB_PORT", "5432"),
        "TEST": {
            "NAME": "test_db",
        },
    },
}
FIXTURE_DIRS = ["fixtures"]

# Haztrak settings
os.environ["HT_RCRAINFO_ENV"] = "PREPROD"
