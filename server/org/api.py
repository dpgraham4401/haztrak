"""REST API for the organization module."""

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from guardian.shortcuts import get_objects_for_user
from ninja import Router

from org.schemas import OrgSchema, SiteSchema

from .models import Org, Site

router = Router(tags=["Organizations"], by_alias=True, exclude_none=True)


@router.get("organizations", response=list[OrgSchema])
def list_orgs(request: HttpRequest):
    """Get a list of organizations."""
    queryset = Org.objects.all()
    user = request.user
    return get_objects_for_user(user, [], queryset, accept_global_perms=False)


@router.get("organizations/{org_id}", response=OrgSchema)
def get_org(request: HttpRequest, org_id: str):
    """Get an organization by slug."""
    qs = get_objects_for_user(request.user, [], Org.objects.filter_by_id(org_id))
    return get_object_or_404(qs)


@router.get("organizations/{org_id}/sites", response=list[SiteSchema])
def get_org_sites(request: HttpRequest, org_id: str):
    """Get an organization's sites."""
    org_query = get_objects_for_user(request.user, [], Org.objects.filter_by_id(org_id))
    org_instance = get_object_or_404(org_query)
    return Site.objects.filter_by_org(org_instance)


@router.get("/sites", response=list[SiteSchema])
def list_sites(request: HttpRequest):
    """Get a list of all sites (temporary)."""
    queryset = Site.objects.all()
    user = request.user
    return get_objects_for_user(user, [], queryset, accept_global_perms=False)
