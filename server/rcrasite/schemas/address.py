"""Address model schema for Django Ninja."""

from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel
from rcrasite.models import RcraCountries, RcraStates


class LocalitySchema(BaseModel):
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


class AddressSchema(BaseModel):
    """Address model schema for JSON representation."""

    street_number: str | None = Field(None, alias="streetNumber")
    address1: str
    address2: str | None = None
    city: str | None = None
    state: LocalitySchema | None = None
    country: LocalitySchema | None = None
    zip: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    @field_validator("state", mode="before")
    @classmethod
    def serialize_state(cls, state: str) -> LocalitySchema:
        return LocalitySchema(code=state, name=RcraStates.from_code(state))

    @field_validator("country", mode="before")
    @classmethod
    def serialize_country(cls, country: str) -> LocalitySchema:
        return LocalitySchema(code=country, name=RcraCountries.from_code(country))
