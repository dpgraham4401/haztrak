"""Address model schema for Django Ninja."""

from ninja import Schema
from pydantic import ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel

from trak.apps.rcrasite.models import RcraCountries, RcraStates


class RcraLocalitySchema(Schema):
    """Represents a RCRAInfo locality (state or country).

    Examples:
        {
            "code": "TX",
            "name": "Texas"
        }.
    """

    code: str = Field(..., description="The locality code, e.g. 'TX'")
    name: str | None = Field(None, description="The full locality name, e.g. 'Texas'")

    model_config = ConfigDict(from_attributes=True)


class RcraAddressSchema(Schema):
    """Address model schema for JSON representation."""

    street_number: str | None = Field(None, alias="streetNumber")
    address1: str
    address2: str | None = None
    city: str | None = None
    state: RcraLocalitySchema | None = None
    country: RcraLocalitySchema | None = None
    zip: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    @field_validator("state", mode="before")
    @classmethod
    def serialize_state(cls, state: str) -> RcraLocalitySchema:
        return RcraLocalitySchema(code=state, name=RcraStates.from_code(state))

    @field_validator("country", mode="before")
    @classmethod
    def serialize_country(cls, country: str) -> RcraLocalitySchema:
        return RcraLocalitySchema(code=country, name=RcraCountries.from_code(country))
