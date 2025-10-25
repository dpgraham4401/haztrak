"""API schemas for the Core app."""

from datetime import datetime

from ninja import ModelSchema
from pydantic import ConfigDict, Field

from core.models import TrakUser


class TrakUserSchema(ModelSchema):
    """Schema for the TrakUser model."""

    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    is_active: bool = Field(alias="isActive")
    date_joined: datetime = Field(alias="dateJoined")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )

    class Meta:
        """Configuration for the TrakUser schema."""

        model = TrakUser
        fields = [
            "id",
            "username",
            "email",
        ]
