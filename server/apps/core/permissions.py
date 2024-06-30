from rest_framework.permissions import BasePermission

from apps.core.models import Authority, UserRole


class SiteAccessPOC(BasePermission):
    """POC using DRF permissions for controlling access to sites"""

    def has_permission(self, request, view):
        try:
            site_id = view.kwargs["epa_id"]
            return UserRole.objects.filter(
                user=request.user, site__rcra_site__epa_id=site_id
            ).exists()
        except KeyError:
            return False
