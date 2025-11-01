"""Signals for the core app."""

from typing import Any

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from profile.models import RcrainfoProfile


@receiver(post_save, sender=User)
def create_profile(sender: Any, instance: Any, created: bool, **kwargs) -> None:
    """Create a profile when a user is created."""
    if created:
        RcrainfoProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender: Any, instance: Any, **kwargs) -> None:
    """Save the profile when the user is saved."""
    instance.profile.save()
