"""Views for the core app."""

from http import HTTPStatus

from django_celery_results.models import TaskResult
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import TrakUser
from core.serializers import TrakUserSerializer
from core.services import get_task_status


class TaskStatusView(APIView):
    """retrieve the status of long-running tasks."""

    queryset = TaskResult.objects.all()

    def get(self, request: Request, task_id: str) -> Response:
        """Retrieve the status of a task."""
        try:
            data = get_task_status(task_id)
            return Response(data=data, status=HTTPStatus.OK)
        except KeyError:
            return Response(
                data={"error": "malformed request"},
                status=HTTPStatus.BAD_REQUEST,
            )
        except ValidationError:
            return Response(
                data={"error": "problem validating request"},
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
            )
        except TaskResult.DoesNotExist:
            return Response(data={"taskId": "unknown"}, status=HTTPStatus.OK)


class GetCurrentTrakUserView(RetrieveAPIView):
    """Get the current user."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TrakUserSerializer

    def get_object(self) -> TrakUser:
        """Get the current user."""
        return self.request.user  # type: ignore[return-value]
