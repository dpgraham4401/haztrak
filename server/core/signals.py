"""Signals for the core app."""

from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from profile.models import Profile, RcrainfoProfile


@receiver(post_save, sender=Profile)
def create_rcrainfo_profile(sender: Any, instance: Profile, created: bool, **kwargs) -> None:
    """Create a profile when a user is created."""
    if created:
        RcrainfoProfile.objects.create(haztrak_profile=instance)  # type: ignore[misc]
