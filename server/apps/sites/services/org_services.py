from apps.sites.models.site_models import HaztrakOrg


def get_org(org_id: str) -> HaztrakOrg:
    """Returns a HaztrakOrg instance or raise an exception"""
    return HaztrakOrg.objects.get(id=org_id)


def get_org_rcrainfo_api_credentials(org_id: str) -> tuple[str, str] | None:
    """Returns a tuple of (rcrainfo_api_id, rcrainfo_api_key)"""
    try:
        org = get_org(org_id)
        if org.is_rcrainfo_integrated:
            return org.rcrainfo_api_id_key
    except HaztrakOrg.DoesNotExist:
        return None
