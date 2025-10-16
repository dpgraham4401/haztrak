"""Schemas for manifest signature data."""

import datetime as dt
from typing import Annotated

from ninja import ModelSchema, Schema
from pydantic import Field
from pydantic.alias_generators import to_camel
from pydantic.config import ConfigDict

from manifest.models import ESignature, PaperSignature, Signer
from rcrasite.schemas.contact import RcraPhoneSchema


class QuickerSignSchema(Schema):
    """Schema for EPA Quicker Sign objects."""

    mtn: Annotated[list[str], Field(..., alias="manifestTrackingNumbers")]
    printed_name: Annotated[str, Field(..., alias="printedSignatureName")]
    printed_date: Annotated[
        dt.datetime,
        Field(
            default_factory=lambda: dt.datetime.now(dt.UTC).isoformat(timespec="milliseconds"),
            alias="printedSignatureDate",
        ),
    ]
    site_type: Annotated[str, Field(..., alias="siteType")]
    site_id: str
    transporter_order: int | None = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class SignerSchema(ModelSchema):
    """Schema for Signer on manifest."""

    rcra_user_id: Annotated[str, Field(..., alias="userId")]
    phone: RcraPhoneSchema

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = Signer
        fields = [
            "first_name",
            "middle_initial",
            "last_name",
            "email",
            "company_name",
            "contact_type",
            "signer_role",
        ]


class ESignatureSchema(ModelSchema):
    """Schema for Electronic Signature on manifest."""

    sign_date: Annotated[dt.datetime, Field(None, alias="signatureDate")]
    signer: SignerSchema

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = ESignature
        fields = [
            # "order
            "cromerr_activity_id",
            "cromerr_document_id",
            "on_behalf",
        ]


class PaperSignatureSchema(ModelSchema):
    """Schema for Paper Signature on manifest."""

    sign_date: Annotated[dt.datetime, Field(None, alias="signatureDate")]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = PaperSignature
        fields = [
            "printed_name",
        ]
