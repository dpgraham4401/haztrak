"""Profile and related schemas."""

from ninja import ModelSchema
from pydantic import ConfigDict

from core.schemas import TrakUserSchema
from profile.models import Profile


class ProfileSchema(ModelSchema):
    """User profile information."""

    # ToDo(David): Consider not user the TraskUserSchema and just serialize the ID
    #  Better modularity, but possibly more network requests.
    user: TrakUserSchema

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )

    class Meta:
        """Metaclass."""

        model = Profile
        fields = [
            "user",
            "avatar",
        ]
