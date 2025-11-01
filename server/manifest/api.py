"""Manifest API endpoints."""

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from manifest.models import Handler, Manifest
from manifest.schemas.handlers import ManifestHandlerSchema
from manifest.schemas.manifest import ManifestSchema

router = Router(tags=["Manifest"], by_alias=True, exclude_none=True)


@router.get("/manifests", response=list[ManifestSchema])
def list_manifest(request: HttpRequest) -> QuerySet[Manifest]:
    """Endpoint to list manifests (temporary)."""
    return Manifest.objects.all()


@router.get("/manifests/handlers", response=list[ManifestHandlerSchema])
def list_handlers(request: HttpRequest) -> QuerySet[Handler]:
    """Endpoint to list manifests (temporary)."""
    return Handler.objects.all()
