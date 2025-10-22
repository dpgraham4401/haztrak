"""A user's RCRAInfo profile schema."""

from typing import Annotated

from ninja import ModelSchema, Schema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel

from profile.models import RcrainfoSiteAccess


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
    """A user's profile retrieved from RCRAInfo."""

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
