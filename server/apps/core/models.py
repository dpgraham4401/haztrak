import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.site.models import Site


class TrakUser(AbstractUser):
    """Haztrak abstract user model. It simply inherits from Django's AbstractUser model."""

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )


class Authority(models.Model):
    name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return f"{self.name}"


class Role(models.Model):
    name = models.CharField(blank=False, max_length=50)
    authority = models.ManyToManyField(Authority)

    def __str__(self):
        return f"{self.name}"


class UserRole(models.Model):
    user = models.OneToOneField(TrakUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.site}"
