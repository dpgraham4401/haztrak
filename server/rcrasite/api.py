"""API endpoints for the RCRA site application."""

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from .models import Address, RcraSite
from .schemas import RcraAddressSchema
from .schemas.rcrasite import RcraSiteSchema

router = Router(tags=["Rcra Sites"], by_alias=True, exclude_none=True)


@router.get("rcrasite/addresses", response=list[RcraAddressSchema])
def list_addresses(request: HttpRequest) -> QuerySet[Address]:
    """Get a list of Address (temporary)."""
    return Address.objects.all()


@router.get("rcrasite", response=list[RcraSiteSchema])
def list_handlers(request: HttpRequest) -> QuerySet[RcraSite]:
    """Get a list of Handler (temporary)."""
    return RcraSite.objects.all()
