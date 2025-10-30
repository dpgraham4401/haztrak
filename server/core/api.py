"""API endpoints for the Core app."""

from http import HTTPStatus

from django.http import HttpRequest
from django_celery_results.models import TaskResult
from ninja import Router
from ninja.errors import AuthenticationError
from rest_framework.exceptions import ValidationError

from core.schemas import ErrorSchema, TaskStatusSchema, TaskUnknownSchema, TrakUserSchema
from core.services import get_task_status

router = Router(tags=["Core"], by_alias=True, exclude_none=True)


@router.get(
    "/users/me",
    response=TrakUserSchema,
)
def get_current_user(request: HttpRequest):
    """Get the currently authenticated user (mirrors DRF GetCurrentTrakUserView)."""
    user = request.user
    if user.is_anonymous:
        raise AuthenticationError(message="Authentication required to access this endpoint.")
    return user


@router.get(
    "/task/{task_id}",
    response={
        HTTPStatus.OK: TaskStatusSchema | TaskUnknownSchema,
        HTTPStatus.BAD_REQUEST: ErrorSchema,
        HTTPStatus.INTERNAL_SERVER_ERROR: ErrorSchema,
    },
)
def get_task_status_view(request, task_id: str):
    """Retrieve the status of a long-running task (mirrors DRF TaskStatusView)."""
    try:
        data = get_task_status(task_id)
        return HTTPStatus.OK, data
    except KeyError:
        return HTTPStatus.BAD_REQUEST, {"error": "malformed request"}
    except ValidationError:
        return HTTPStatus.INTERNAL_SERVER_ERROR, {"error": "problem validating request"}
    except TaskResult.DoesNotExist:
        return HTTPStatus.OK, {"taskId": "unknown"}
