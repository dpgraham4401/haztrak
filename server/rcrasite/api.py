"""API endpoints for the RCRA site application."""

from ninja import Router

from .models import Address, RcraSite
from .schemas import RcraAddressSchema
from .schemas.handler import RcraHandlerSchema

router = Router(tags=["Handler"], by_alias=True)


@router.get("/address", response=list[RcraAddressSchema])
def list_addresses(request):
    """Get a list of Address (temporary)."""
    return Address.objects.all()


@router.get("", response=list[RcraHandlerSchema])
def list_handlers(request):
    """Get a list of Handler (temporary)."""
    return RcraSite.objects.all()
