"""RCRAInfo Manifest schemas."""

from typing import Annotated

from ninja import ModelSchema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel

from manifest.models import Manifest
from manifest.schemas.additional_info import AdditionalInfoSchema
from manifest.schemas.handlers import ManifestHandlerSchema


class ManifestSchema(ModelSchema):
    """Schema for Manifest."""

    mtn: Annotated[str, Field(..., alias="manifestTrackingNumber")]
    generator: ManifestHandlerSchema
    transporters: list[ManifestHandlerSchema]
    tsdf: ManifestHandlerSchema = Field(..., alias="designatedFacility")
    residue_new_mtn: Annotated[
        list[str] | None, Field(None, alias="residueNewManifestTrackingNumbers")
    ]
    import_flag: Annotated[bool, Field(..., alias="import")]
    contains_residue_or_rejection: Annotated[
        bool | None, Field(..., alias="containsPreviousRejectOrResidue")
    ]
    additional_info: AdditionalInfoSchema | None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = Manifest
        fields = [
            "created_date",
            "update_date",
            "mtn",
            "status",
            "submission_type",
            "signature_status",
            "origin_type",
            "shipped_date",
            "potential_ship_date",
            "received_date",
            "certified_date",
            "certified_by",
            "broker",
            # "wastes",
            "rejection",
            "rejection_info",
            "discrepancy",
            "residue",
            "residue_new_mtn",
            "import_info",
            "printed_document",
            "form_document",
            "ppc_status",
            # mtnValidationInfo - ToDo
            # provideImageGeneratorInfo - ToDo
            "locked",
            "lock_reason",
        ]
