"""API endpoints for the RCRA site application."""

from ninja import Router

from .models import Address
from .schemas import AddressSchema

router = Router(tags=["Handler"], by_alias=True)


@router.get("/address", response=list[AddressSchema])
def list_addresses(request):
    """Get a list of Address (temporary)."""
    return Address.objects.all()
