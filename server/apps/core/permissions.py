from rest_framework.permissions import BasePermission


class SiteAccessPOC(BasePermission):
    """POC using DRF permissions for controlling access to sites"""

    def has_permission(self, request, view):
        print("site access poc has permissions")
        return True
