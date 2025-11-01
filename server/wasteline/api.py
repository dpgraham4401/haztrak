"""WasteLine API handlers."""

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from wasteline.models import WasteLine
from wasteline.schemas import WastelineSchema

router = Router(tags=["wasteline"], by_alias=True, exclude_none=True)


@router.get("/wastelines", response=list[WastelineSchema])
def list_wastelines(request: HttpRequest) -> QuerySet[WasteLine]:
    """List all WasteLines (temporary)."""
    return WasteLine.objects.all()
