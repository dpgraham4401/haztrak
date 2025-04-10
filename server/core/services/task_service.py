"""Service class for interacting with the Task model layer and celery tasks."""

import logging
from typing import TYPE_CHECKING

from core.serializers import TaskStatusSerializer
from core.tasks import example_task
from django.core.cache import CacheKeyWarning, cache
from django_celery_results.models import TaskResult
from rest_framework.exceptions import ValidationError
from rest_framework.utils.serializer_helpers import ReturnDict

if TYPE_CHECKING:
    from celery.result import AsyncResult

logger = logging.getLogger(__name__)


def get_task_status(task_id: str) -> ReturnDict:
    """Gets the status of a long-running celery task from the cache or the database."""
    cache_data: dict | None = _get_cached_status(task_id)
    if cache_data is not None:
        return _parse_status(cache_data)
    return get_task_results(task_id)


def get_task_results(task_id: str) -> ReturnDict:
    """Gets the results of a long-running celery task stored in the database."""
    task_results = TaskResult.objects.get(task_id=task_id)
    task_serializer = TaskStatusSerializer(task_results)
    return task_serializer.data


def _get_cached_status(task_id: str) -> dict | None:
    """Gets the status of a long-running celery task from our key-value store."""
    try:
        cache_data = cache.get(task_id)
        if cache_data is not None:
            return cache_data
    except CacheKeyWarning:
        return None


def _parse_status(task_status: dict) -> ReturnDict:
    task_serializer = TaskStatusSerializer(data=task_status)
    if task_serializer.is_valid():
        return task_serializer.data
    raise ValidationError(task_serializer.errors)


def launch_example_task() -> str | None:
    """Launches an example long-running celery task."""
    try:
        task: AsyncResult = example_task.delay()
    except KeyError:
        return None
    else:
        return task.id


class TaskService:
    """Service class for interacting with the Task model layer and celery tasks."""

    def __init__(
        self,
        task_id: str,
        task_name: str,
        status: str = "PENDING",
        result: dict | None = None,
    ):
        self.task_id = task_id
        self.task_name = task_name
        self.status = status
        self.result = result

    @classmethod
    def get_task_status(cls, task_id) -> ReturnDict:
        """Gets the status of a long-running celery task from the cache or the database."""
        cache_data = cls._get_cached_status(task_id)
        if cache_data is not None:
            return cls._parse_status(cache_data)
        return cls.get_task_results(task_id)

    @staticmethod
    def get_task_results(task_id: str) -> ReturnDict:
        """Gets the results of a long-running celery task stored in the database."""
        task_results = TaskResult.objects.get(task_id=task_id)
        task_serializer = TaskStatusSerializer(task_results)
        return task_serializer.data

    @staticmethod
    def _parse_status(task_status: dict) -> ReturnDict:
        task_serializer = TaskStatusSerializer(data=task_status)
        if task_serializer.is_valid():
            return task_serializer.data
        raise ValidationError(task_serializer.errors)

    @staticmethod
    def _get_cached_status(task_id: str) -> dict | None:
        """Gets the status of a long-running celery task from our key-value store.

        If not found or error, returns None
        """
        try:
            cache_data = cache.get(task_id)
            if cache_data is not None:
                return cache_data
        except CacheKeyWarning:
            return None

    @staticmethod
    def launch_example_task() -> str | None:
        """Launches an example long-running celery task."""
        try:
            task: AsyncResult = example_task.delay()
        except KeyError:
            return None
        else:
            return task.id

    def update_task_status(self, status: str, results: dict | None = None) -> object | None:
        """Updates the status of a long-running celery task in our key-value store.

        Returns an error or None.
        """
        if results:
            self.result = results
        try:
            task_serializer = TaskStatusSerializer(
                data={
                    "taskId": self.task_id,
                    "status": status,
                    "taskName": self.task_name,
                    "result": self.result,
                },
            )
            if task_serializer.is_valid():
                logger.debug(f"task_serializer.data: {task_serializer.data}")
                cache.set(self.task_id, task_serializer.data)
                return task_serializer.data
            logger.error(f"Could not serialize task status: {task_serializer.errors}")
        except CacheKeyWarning as exc:
            msg = f"CacheKeyWarning while updating task status {exc}"
            logger.exception(msg)
            return exc
        else:
            return None
