"""API endpoints for the Core app."""

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from core.models import TrakUser
from core.schemas import TrakUserSchema

router = Router(tags=["Core"], by_alias=True, exclude_none=True)


@router.get("/users", response=list[TrakUserSchema])
def list_users(request: HttpRequest) -> QuerySet[TrakUser]:
    """Endpoint to list users."""
    return TrakUser.objects.all()
