"""A user's RCRAInfo profile schema."""

from ninja import ModelSchema
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from profile.models import RcrainfoProfile


class RcrainfoProfileSchema(ModelSchema):
    """A user's profile retrieved from RCRAInfo."""

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

    class Meta:
        """Metaclass."""

        model = RcrainfoProfile
        fields = [
            "id",
            "rcra_username",
            "phone_number",
            "email",
        ]
