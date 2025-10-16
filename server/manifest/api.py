"""Manifest API endpoints."""

from ninja import Router

from manifest.models import Handler
from manifest.schemas.handlers import ManifestHandlerSchema

router = Router(tags=["Manifest"], by_alias=True)


@router.get("/manifests/handlers", response=list[ManifestHandlerSchema])
def list_manifests(request):
    """Endpoint to list manifests (temporary)."""
    return Handler.objects.all()
