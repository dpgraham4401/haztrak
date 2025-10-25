"""A user's RCRAInfo profile schema."""

from typing import Annotated

from ninja import ModelSchema, Schema
from pydantic import ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel

from trak.apps.profile.models import RcrainfoSiteAccess


class RcrainfoSitePermissionsInternalSchema(ModelSchema):
    """RcrainfoSiteAccess model serializer.

    We use this internally because it's easier to handle,
    Using consistent naming,Haztrak has a separate serializer for user permissions from RCRAInfo.
    """

    site: Annotated[str, Field(..., alias="epaSiteId")]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = RcrainfoSiteAccess
        fields = [
            "site",
            "site_manager",
            "annual_report",
            "biennial_report",
            "e_manifest",
            "wiets",
            "my_rcra_id",
        ]


class RcrainfoProfileSchema(Schema):
    """A user's profile retrieved from RCRAInfo.

    We use this internally because it's easier to handle,
    Using consistent naming,Haztrak has a separate serializer for user permissions from RCRAInfo.
    """

    has_rcrainfo_api_id_key: Annotated[bool, Field(..., alias="apiUser")]
    permissions: Annotated[
        list[RcrainfoSitePermissionsInternalSchema],
        Field(..., alias="rcraSites"),
    ]
    rcra_username: str | None
    phone_number: str | None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class RcrainfoModuleAccessSchema(Schema):
    """Represents a single permission entry from RCRAInfo JSON."""

    module: str
    level: str | bool

    @field_validator("level", mode="before")
    @classmethod
    def validate_level(cls, level: str) -> str | bool:
        """Convert module permission level to our internal value."""
        site_management_strings = ["Active", "Inactive"]
        if level in site_management_strings:
            return level == "Active"
        return level


class RcrainfoSiteAccessSchema(Schema):
    """Top-level RCRAInfo site access schema."""

    site_id: Annotated[str, Field(..., alias="siteId")]
    site_name: Annotated[str, Field(..., alias="siteName")]
    permissions: list[RcrainfoModuleAccessSchema]
