"""REST API for the organization module."""

from ninja import Router
from org.schemas import OrgSchema

from .models import Org

router = Router(tags=["Organizations"], by_alias=True)


@router.get("", response=list[OrgSchema])
def list_orgs(request):
    """Get a list of organizations."""
    return Org.objects.all()
