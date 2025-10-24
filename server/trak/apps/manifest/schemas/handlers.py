"""Uniform manifest handler schema definitions."""

from typing import Annotated

from ninja import Schema
from pydantic import AliasChoices, ConfigDict, Field
from pydantic.alias_generators import to_camel

from trak.apps.manifest.models import Handler
from trak.apps.manifest.schemas.signatures import ESignatureSchema, PaperSignatureSchema
from trak.apps.rcrasite.schemas import RcraAddressSchema
from trak.apps.rcrasite.schemas.contact import RcraContactSchema


class ManifestPhoneSchema(Schema):
    """Schema for manifest phone."""

    number: str
    extension: str | None = None


class ManifestHandlerSchema(Schema):
    """Schema for manifest handler.

    This schema flattens the RcraSite information
    (e.g., data that is relevant to the site, not manifest specific) into the handler schema.
    """

    # Fields from RcraSite are flattened to follow RCRAInfo's e-Manifest structure.
    epa_id: Annotated[
        str,
        Field(
            ..., alias="epaSiteId", validation_alias=AliasChoices("epaSiteId", "rcra_site.epa_id")
        ),
    ]
    name: Annotated[str, Field(..., validation_alias=AliasChoices("name", "rcra_site.name"))]
    site_type: Annotated[
        str, Field(..., validation_alias=AliasChoices("siteType", "rcra_site.site_type"))
    ]
    site_address: Annotated[
        RcraAddressSchema,
        Field(..., validation_alias=AliasChoices("siteAddress", "rcra_site.site_address")),
    ]
    mail_address: Annotated[
        RcraAddressSchema,
        Field(..., validation_alias=AliasChoices("mailAddress", "rcra_site.mail_address")),
    ]
    contact: Annotated[
        RcraContactSchema,
        Field(..., validation_alias=AliasChoices("contact", "rcra_site.contact")),
    ]
    gis_primary: Annotated[
        bool, Field(..., validation_alias=AliasChoices("gisPrimary", "rcra_site.gis_primary"))
    ]
    can_esign: Annotated[
        bool, Field(..., validation_alias=AliasChoices("canEsign", "rcra_site.can_esign"))
    ]
    registered_emanifest_user: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "hasRegisteredEmanifestUser", "rcra_site.registered_emanifest_user"
            ),
        ),
    ]
    limited_esign: Annotated[
        bool, Field(..., validation_alias=AliasChoices("limitedEsign", "rcra_site.limited_esign"))
    ]

    emergency_phone: ManifestPhoneSchema | None
    paper_signature: Annotated[
        PaperSignatureSchema | None, Field(None, alias="paperSignatureInfo")
    ]
    electronic_signature: Annotated[
        list[ESignatureSchema] | None, Field(None, alias="electronicSignatureInfo")
    ]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = Handler
        exclude = ["rcra_site"]
