"""WasteLine API handlers."""

from ninja import Router

from wasteline.models import WasteLine
from wasteline.schemas import WastelineSchema

router = Router(tags=["wasteline"], by_alias=True, exclude_none=True)


@router.get("/wastelines", response=list[WastelineSchema])
def list_wastelines(request):
    """List all WasteLines."""
    return WasteLine.objects.all()
