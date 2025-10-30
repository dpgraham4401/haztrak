"""Organization and Site models."""

import uuid
from typing import TYPE_CHECKING

from django.conf import settings
from django.db import models
from django.db.models import Manager, Model, QuerySet
from django_extensions.db.fields import AutoSlugField
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from guardian.shortcuts import get_objects_for_user

from core.models import TrakUser
from profile.models import RcrainfoProfile

if TYPE_CHECKING:
    pass


class OrgManager(Manager["Org"]):
    """Organization Repository manager."""

    def get_by_username(self, username: str) -> "Org | None":
        """Get the organization for a user."""
        user = TrakUser.objects.get(username=username)
        # TODO(David): Currently we are assuming the use only has one org
        orgs: QuerySet[Org] = get_objects_for_user(
            user,
            "view_org",
            self.model,
            accept_global_perms=False,
        )
        return orgs.first()

    def get_by_slug(self, slug: str) -> "Org":
        """Get an organization by slug."""
        return self.model.objects.get(slug=slug)

    def filter_by_slug(self, slug: str) -> QuerySet["Org"]:
        """Return a queryset filtering organization by slug.

        Useful for cases where a queryset object is needed instead of an instance.

        See Also:
            get_by_slug - which returns a single org or raises DoesNotExist
        """
        return self.model.objects.filter(slug=slug)

    def filter_by_id(self, id: str) -> QuerySet["Org"]:
        """Return a queryset filtering organization by id.

        Useful for cases where a queryset object is needed instead of an instance.

        See Also:
            filter_by_slug - which returns a single org or raises DoesNotExist
        """
        return self.model.objects.filter(id=id)


class Org(Model):
    """Haztrak Organization."""

    id = models.UUIDField(
        unique=True,
        editable=False,
        primary_key=True,
        default=uuid.uuid4,
    )
    slug = AutoSlugField(
        populate_from="name",
        max_length=50,
        null=False,
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False,
    )
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    objects = OrgManager()

    class Meta:
        """Metaclass."""

        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ["name"]
        indexes = [models.Index(fields=["slug"], name="org_slug_idx")]

    def __str__(self):
        """Human-readable representation."""
        return f"{self.name}"

    @property
    def rcrainfo_api_id_key(self) -> tuple[str | None, str | None]:
        """Returns the RcraInfo API credentials for the admin user."""
        try:
            rcrainfo_profile = RcrainfoProfile.objects.get(haztrak_profile__user=self.admin)
        except RcrainfoProfile.DoesNotExist:
            return None, None
        else:
            return rcrainfo_profile.rcra_api_id, rcrainfo_profile.rcra_api_key

    @property
    def is_rcrainfo_integrated(self) -> bool:
        """Returns True if the admin user has RcraInfo API credentials."""
        if RcrainfoProfile.objects.filter(haztrak_profile__user=self.admin).exists():
            return RcrainfoProfile.objects.get(
                haztrak_profile__user=self.admin,
            ).has_rcrainfo_api_id_key
        return False


class OrgUserObjectPermission(UserObjectPermissionBase):
    """Org object level permission."""

    class Meta(UserObjectPermissionBase.Meta):
        """Metaclass."""

        verbose_name = "Org Permission"
        verbose_name_plural = "Org Permissions"

    # Note: class attribute must be named content_object (see django-guardian docs)
    content_object = models.ForeignKey(Org, on_delete=models.CASCADE, db_column="org_object_id")


class OrgGroupObjectPermission(GroupObjectPermissionBase):
    """Org object level Group."""

    class Meta(GroupObjectPermissionBase.Meta):
        """Metaclass."""

        verbose_name = "Org Role"
        verbose_name_plural = "Org Roles"

    content_object = models.ForeignKey(Org, on_delete=models.CASCADE, db_column="org_object_id")
