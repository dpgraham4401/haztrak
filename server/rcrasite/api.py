"""API endpoints for the RCRA site application."""

from ninja import Router

from .models import Address, RcraSite
from .schemas import AddressSchema
from .schemas.handler import HandlerSchema

router = Router(tags=["Handler"], by_alias=True)


@router.get("/address", response=list[AddressSchema])
def list_addresses(request):
    """Get a list of Address (temporary)."""
    return Address.objects.all()


@router.get("", response=list[HandlerSchema])
def list_handlers(request):
    """Get a list of Handler (temporary)."""
    return RcraSite.objects.all()
