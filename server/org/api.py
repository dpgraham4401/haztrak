"""REST API for the organization module."""

from django.shortcuts import get_object_or_404
from ninja import Router
from org.schemas import OrgSchema

from .models import Org

router = Router(tags=["Organizations"], by_alias=True)


@router.get("", response=list[OrgSchema])
def list_orgs(request):
    """Get a list of organizations."""
    return Org.objects.all()


@router.get("/{org_slug}", response=OrgSchema)
def get_org(request, org_slug: str):
    """Get an organization by slug."""
    return get_object_or_404(Org.objects.all(), slug=org_slug)
