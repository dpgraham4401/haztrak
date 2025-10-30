"""API schemas for the Core app."""

from datetime import datetime
from typing import Any, Literal

from ninja import ModelSchema, Schema
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


class ErrorSchema(Schema):
    """Generic error response schema."""

    error: str


class TaskStatusSchema(Schema):
    """Schema representing the status of a long-running task."""

    task_id: str
    task_name: str
    status: Literal["PENDING", "STARTED", "SUCCESS", "FAILURE", "NOT FOUND"]
    created_date: datetime | None = None
    done_date: datetime | None = None
    result: dict[str, Any] | list[Any] | None = None


class TaskUnknownSchema(Schema):
    """Schema used when a taskId is unknown."""

    task_id: str
