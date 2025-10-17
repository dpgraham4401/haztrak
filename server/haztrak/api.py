"""Bring together API routers."""

from ninja import NinjaAPI
from ninja.security import django_auth

api_auth = [django_auth]


api = NinjaAPI(
    title="Haztrak API",
    description="Access Haztrak through the REST API.",
    auth=api_auth,
    servers=[],
    urls_namespace="api",
)
