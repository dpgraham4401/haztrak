"""Schema for RCRAInfo handler permissions."""

from ninja import Schema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel


class RcraSitePermissionSchema(Schema):
    """RCRAInfo Site Permission Schema.

    We use this internally because it's easier to handle,
    Using consistent naming,Haztrak has a separate schema for user permissions from RCRAInfo.
    """

    epa_site_id: str
    site_management: bool
    annual_report: str
    biennial_report: str
    e_manifest: str
    wiets: str = Field(alias="WIETS")
    my_rcra_id: str = Field(alias="myRCRAid")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class RcrainfoModulePermissionSchema(Schema):
    """RCRAInfo module permission.

    This Schema represents a single module permission in RCRAInfo.
    It's defined by the RCRAInfo API.
    """

    module: str
    level: str


class RcrainfoHandlerPermissionsSchema(Schema):
    """RCRAInfo Handler Permissions Schema.

    This Schema represents the permissions for a site in RCRAInfo.
    It's defined by the RCRAInfo API.
    """

    site_id: str
    permissions: list[RcrainfoModulePermissionSchema]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )
