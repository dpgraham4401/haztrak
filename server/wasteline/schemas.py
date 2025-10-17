"""Wasteline schemas."""

from typing import Annotated

from ninja import ModelSchema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel

from wasteline.models import WasteLine


class WastelineSchema(ModelSchema):
    """Wasteline schema."""

    dot_info: Annotated[dict | None, Field(None, alias="dotInformation")]
    discrepancy_info: Annotated[dict | None, Field(None, alias="discrepancyResidueInfo")]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = WasteLine
        fields = [
            "line_number",
            "dot_hazardous",
            "dot_info",
            "quantity",
            "hazardous_waste",
            "br",
            "br_info",
            "management_method",
            "pcb",
            "pcb_infos",
            "epa_waste",
        ]
