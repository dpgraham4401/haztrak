"""schemas for Org and Site."""

from typing import Annotated
from uuid import UUID

from ninja import ModelSchema, Schema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel

from org.models import Site


class OrgSchema(Schema):
    """Haztrak Organization schema."""

    id: UUID
    name: str
    slug: str
    is_rcrainfo_integrated: bool = Field(alias="rcrainfoIntegrated")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class SiteSchema(ModelSchema):
    """Haztrak Site schema."""

    name: str
    rcra_site_id: Annotated[int, Field(..., alias="rcraSite")]
    org_id: Annotated[UUID, Field(..., alias="organization")]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass"""

        model = Site
        exclude = [
            "rcra_site",
            "org",
            "id",
        ]
