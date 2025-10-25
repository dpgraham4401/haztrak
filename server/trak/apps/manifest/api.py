"""Manifest API endpoints."""

from ninja import Router

from trak.apps.manifest.models import Handler, Manifest
from trak.apps.manifest.schemas.handlers import ManifestHandlerSchema
from trak.apps.manifest.schemas.manifest import ManifestSchema

router = Router(tags=["Manifest"], by_alias=True, exclude_none=True)


@router.get("/manifests", response=list[ManifestSchema])
def list_manifest(request):
    """Endpoint to list manifests (temporary)."""
    return Manifest.objects.all()


@router.get("/manifests/handlers", response=list[ManifestHandlerSchema])
def list_handlers(request):
    """Endpoint to list manifests (temporary)."""
    return Handler.objects.all()
