"""Address model schema for Django Ninja."""

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class Locality(BaseModel):
    """Represents a RCRAInfo locality (state or country).

    Examples:
        {
            "code": "TX",
            "name": "Texas"
        }.
    """

    code: str = Field(..., description="The locality code, e.g. 'TX'")
    name: str | None = Field(None, description="The full locality name, e.g. 'Texas'")


class AddressSchema(BaseModel):
    """Address model schema for JSON representation."""

    street_number: str | None = Field(None, alias="streetNumber")
    address1: str
    address2: str | None = None
    city: str | None = None
    # state: Locality | None = None
    # country: Locality | None = None
    zip: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )
