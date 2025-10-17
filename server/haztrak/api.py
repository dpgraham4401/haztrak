"""Bring together API routers."""

from ninja import NinjaAPI
from ninja.security import django_auth
from org.api import router as org_router
from rcrasite.api import router as rcrasite_router

api_auth = [django_auth]


api = NinjaAPI(
    title="Haztrak API",
    description="Access Haztrak through the REST API.",
    auth=api_auth,
    servers=[],
    urls_namespace="api",
)

api.add_router("/organizations", org_router)
api.add_router("/handler", rcrasite_router)
