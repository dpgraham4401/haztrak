"""schemas for Org and Site."""

import uuid

from ninja import Schema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel
from rcrasite.schemas.handler import RcraHandlerSchema


class OrgSchema(Schema):
    """Haztrak Organization schema."""

    id: uuid.UUID
    name: str
    slug: str
    is_rcrainfo_integrated: bool = Field(alias="rcrainfoIntegrated")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class SiteSchema(Schema):
    """Haztrak Site schema."""

    name: str
    rcra_site: RcraHandlerSchema = Field(alias="handler")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )
