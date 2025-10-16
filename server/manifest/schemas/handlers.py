"""Uniform manifest handler schema definitions."""

from ninja import Schema
from pydantic import AliasChoices, ConfigDict, Field
from pydantic.alias_generators import to_camel

from manifest.models import Handler


class ManifestPhoneSchema(Schema):
    """Schema for manifest phone."""

    number: str
    extension: str | None = None


class ManifestHandlerSchema(Schema):
    """Schema for manifest handler."""

    # rcra_site: RcraHandlerSchema
    epa_id: str = Field(
        ..., alias="epaSiteId", validation_alias=AliasChoices("epaSiteId", "rcra_site.epa_id")
    )
    emergency_phone: ManifestPhoneSchema | None
    paper_signature: dict | None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = Handler
        exclude = ["rcra_site"]
