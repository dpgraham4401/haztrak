"""RCRAInfo 'additional info' manifest schemas."""

from typing import Annotated

from ninja import ModelSchema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel

from trak.apps.manifest.models import AdditionalInfo


class AdditionalInfoSchema(ModelSchema):
    """Schema for Additional Info on manifest."""

    original_mtn: Annotated[list[str] | None, Field(None, alias="originalManifestTrackingNumbers")]
    new_destination: Annotated[str | None, Field(None, alias="newManifestDestination")]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = AdditionalInfo
        fields = [
            "consent_number",
            "comments",
            "handling_instructions",
        ]
