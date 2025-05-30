"""Core models."""

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from guardian.mixins import GuardianUserMixin


class TrakUser(GuardianUserMixin, AbstractUser):
    """Haztrak abstract user model. It simply inherits from Django's AbstractUser model."""

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    class Meta:
        """Metaclass."""

        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]

    def has_perm(self, perm, obj=None):
        """Check if user has permission."""
        return super().has_perm(perm, obj)
