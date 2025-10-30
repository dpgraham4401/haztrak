"""Organization and Site models."""

from typing import TYPE_CHECKING
from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import QuerySet
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from guardian.shortcuts import get_objects_for_user

from core.models import TrakUser

if TYPE_CHECKING:
    from org.models import Org


class SiteManager(QuerySet):
    """Query interface for the Site model."""

    def filter_by_username(self, username: str) -> QuerySet["Site"]:
        """Filter a list of sites a user has access to (by username)."""
        return get_objects_for_user(
            TrakUser.objects.get(username=username),
            "view_site",
            self.model,
            accept_global_perms=False,
        )

    def get_by_user_and_epa_id(self, user: "AbstractBaseUser", epa_id: str) -> "Site":
        """Get a site by EPA ID number that a user has access to."""
        combined_filter: QuerySet = self.filter_by_user(user) & self.filter_by_epa_ids(epa_id)
        return combined_filter.get()

    def get_by_username_and_epa_id(self, username: str, epa_id: str) -> "Site":
        """Get a site by EPA ID number that a user has access to."""
        combined_filter: QuerySet = self.filter_by_username(username) & self.filter_by_epa_ids(
            epa_id,
        )
        return combined_filter.get()

    def filter_by_user(self, user: "AbstractBaseUser") -> QuerySet["Site"]:
        """Filter a list of sites a user has access to (by user object)."""
        return get_objects_for_user(user, "view_site", self.model, accept_global_perms=False)

    def filter_by_epa_ids(self, epa_ids: list[str] | str) -> QuerySet["Site"]:
        """Filter a sites by EPA ID number."""
        if isinstance(epa_ids, str):
            epa_ids = [epa_ids]
        return self.filter(rcra_site__epa_id__in=epa_ids)

    def get_by_epa_id(self, epa_id: str) -> "Site":
        """Get a site by RCRAInfo EPA ID number. Throws Site.DoesNotExist if not found."""
        return self.filter_by_epa_ids(epa_id).get()

    def filter_by_org(self, org: "Org") -> QuerySet["Site"]:
        """Get a list of sites by organization."""
        return self.filter(org=org)

    def filter_by_id(self, idx: int) -> QuerySet["Site"]:
        """Get a list of sites by organization."""
        return self.filter(id=idx)


class Site(models.Model):
    """The site entity represents a physical location that is a part of an organization."""

    id = models.UUIDField(
        unique=True,
        editable=False,
        primary_key=True,
        default=uuid4,
    )
    name = models.CharField(
        verbose_name="site alias",
        max_length=200,
        validators=[MinLengthValidator(2, "site aliases must be longer than 2 characters")],
    )
    rcra_site = models.OneToOneField(
        verbose_name="rcra_site",
        to="rcrasite.RcraSite",
        on_delete=models.CASCADE,
    )
    last_rcrainfo_manifest_sync = models.DateTimeField(
        verbose_name="last RCRAInfo manifest sync date",
        null=True,
        blank=True,
    )
    org = models.ForeignKey(
        "org.Org",
        on_delete=models.CASCADE,
    )

    objects = SiteManager.as_manager()

    class Meta:
        """Metaclass."""

        verbose_name = "Site"
        verbose_name_plural = "Sites"
        ordering = ["rcra_site__epa_id"]

    def __str__(self):
        """
        Human-readable representation.

        Used in StringRelated fields in serializer classes.
        """
        return f"{self.rcra_site.epa_id}"

    @property
    def epa_id(self):
        """EPA ID number of the site."""
        return self.rcra_site.epa_id

    @property
    def admin_has_rcrainfo_api_credentials(self) -> bool:
        """Returns True if the admin user has RcraInfo API credentials."""
        return self.org.is_rcrainfo_integrated


class SiteUserObjectPermission(UserObjectPermissionBase):
    """Site object level permission."""

    class Meta(UserObjectPermissionBase.Meta):
        """Metaclass."""

        verbose_name = "Site Permission"
        verbose_name_plural = "Site Permissions"

    content_object = models.ForeignKey(Site, on_delete=models.CASCADE, db_column="site_object_id")


class SiteGroupObjectPermission(GroupObjectPermissionBase):
    """Site object level Group."""

    class Meta(GroupObjectPermissionBase.Meta):
        """Metaclass."""

        verbose_name = "Site Role"
        verbose_name_plural = "Site Roles"

    content_object = models.ForeignKey(Site, on_delete=models.CASCADE, db_column="site_object_id")
