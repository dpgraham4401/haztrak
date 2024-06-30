from rest_framework.permissions import BasePermission

from apps.core.models import Authority, UserRole


class SiteAccessPOC(BasePermission):
    """POC using DRF permissions for controlling access to sites"""

    allowed_authorities = ["read", "edit", "sign"]

    def has_permission(self, request, view):
        try:
            site_id = view.kwargs["epa_id"]
            authorities = Authority.objects.filter(
                role__userrole__user=request.user,
                role__userrole__site__rcra_site__epa_id__iexact=site_id,
            )
            authority_names = [i.name for i in authorities]
            return any(name in self.allowed_authorities for name in authority_names)
        except KeyError:
            return False
