"""Handler Schema serializer."""

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from rcrasite.schemas import RcraAddressSchema
from rcrasite.schemas.contact import RcraContactSchema, RcraPhoneSchema


class RcraHandlerSchema(BaseModel):
    """Schema for serializing and deserializing handler information."""

    epa_id: str = Field(..., alias="epaSiteId")
    site_type: str | None = Field(None, alias="siteType")
    modified: bool = Field(False)
    name: str = Field(..., description="The name of the handler.")
    site_address: RcraAddressSchema
    mail_address: RcraAddressSchema
    contact: RcraContactSchema
    emergency_phone: RcraPhoneSchema | None
    limited_esign: bool = Field(False)
    can_esign: bool = Field(False)
    registered_emanifest_user: bool = Field(False)
    gis_primary: bool = Field(False)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )
