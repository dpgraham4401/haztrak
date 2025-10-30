"""Bring together API routers."""

from ninja import NinjaAPI, Router

from core.api import router as core_router
from manifest.api import router as manifest_router
from org.api import router as org_router
from profile.api import router as profile_router
from rcrasite.api import router as rcrasite_router
from wasteline.api import router as wasteline_router

api = NinjaAPI(
    title="Haztrak API",
    description="Access Haztrak through the REST API.",
    servers=[],
    urls_namespace="api",
)

rcrainfo_router = Router()
rcrainfo_router.add_router("", rcrasite_router)
rcrainfo_router.add_router("", manifest_router)
rcrainfo_router.add_router("", wasteline_router)

api.add_router("", core_router)
api.add_router("", org_router)
api.add_router("", profile_router)
api.add_router("/rcra", rcrainfo_router)
