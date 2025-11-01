"""Celery tasks for the wasteline app."""

import logging

from celery import Task, shared_task, states
from celery.exceptions import Ignore, Reject

logger = logging.getLogger(__name__)


@shared_task(name="pull_federal_code", bind=True)
def pull_federal_codes_task(self: Task, api_user: str | None = None) -> None:
    """Pull federal waste codes from the EPA API."""
    from core.services import get_rcra_client

    msg = "start task {self.name}"
    logger.debug(msg)
    try:
        rcrainfo = get_rcra_client(username=api_user)
        return rcrainfo.sync_federal_waste_codes()  # type: ignore[union-attr]
    except (ConnectionError, TimeoutError) as exc:
        raise Reject from exc
    except Exception as exc:
        self.update_state(state=states.FAILURE, meta={"error": "unknown error: {exc}"})
        raise Ignore from exc
