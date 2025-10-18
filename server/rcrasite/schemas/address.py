"""Address model schema for Django Ninja."""

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic.alias_generators import to_camel
from rcrasite.models import RcraStates


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

    @model_validator(mode="before")
    @classmethod
    def coerce_locality(cls, value):
        """Allow 'TX', {'code': 'TX'}, or {'code': 'TX', 'name': 'Texas'}."""
        if isinstance(value, cls):
            return value
        if isinstance(value, str):
            name = RcraStates.from_state_code(value)
            if not name:
                raise ValueError(f"Invalid state code: {value}")
            return {"code": value, "name": name}
        if isinstance(value, dict):
            code = value.get("code")
            name = value.get("name") or RcraStates.from_state_code(code)
            return {"code": code, "name": name}
        if value is None:
            return value
        raise TypeError(f"Cannot coerce {value!r} into LocalitySchema")


class AddressSchema(BaseModel):
    """Address model schema for JSON representation."""

    street_number: str | None = Field(None, alias="streetNumber")
    address1: str
    address2: str | None = None
    city: str | None = None
    state: LocalitySchema | None = None
    # country: Locality | None = None
    zip: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )
