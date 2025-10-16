"""Handler Schema serializer."""

from ninja import Schema
from pydantic import ConfigDict, Field
from pydantic.alias_generators import to_camel

from rcrasite.schemas import RcraAddressSchema
from rcrasite.schemas.contact import RcraContactSchema, RcraPhoneSchema


class RcraHandlerSchema(Schema):
    """Schema for serializing and deserializing handler information."""

    epa_id: str = Field(..., alias="epaSiteId")
    site_type: str | None = None
    modified: bool = False
    name: str = Field(..., description="The name of the handler.")
    site_address: RcraAddressSchema
    mail_address: RcraAddressSchema
    contact: RcraContactSchema
    emergency_phone: RcraPhoneSchema | None
    limited_esign: bool = False
    can_esign: bool = False
    registered_emanifest_user: bool = False
    registered: bool = False
    gis_primary: bool = False

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )
