"""RCRAInfo Contact Schema."""

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class RcraPhoneSchema(BaseModel):
    """Schema for RCRAInfo phone information."""

    number: str
    extension: str | None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class RcraContactSchema(BaseModel):
    """Schema for RCRAInfo contact information."""

    first_name: str | None
    middle_initial: str | None
    last_name: str | None
    phone: RcraPhoneSchema | None
    email: str | None
    company_name: str | None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )
