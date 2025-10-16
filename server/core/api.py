"""API endpoints for the Core app."""

from ninja import Router

from core.models import TrakUser
from core.schemas import TrakUserSchema

router = Router(tags=["Core"], by_alias=True)


@router.get("/users", response=list[TrakUserSchema])
def list_users(request):
    """Endpoint to list users."""
    return TrakUser.objects.all()
