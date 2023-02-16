from django.db import models

from .rcra_profile import RcraProfile
from .site import Site

EPA_PERMISSION_LEVEL = [
    ('Certifier', 'Certifier'),
    ('Preparer', 'Preparer'),
    ('Viewer', 'Viewer'),
]


class SitePermission(models.Model):
    """
    RCRAInfo Site Permissions per module connected to a user's RcraProfile
    and the corresponding Site
    """
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        RcraProfile,
        on_delete=models.PROTECT,
        related_name='site_permission'
    )
    site_manager = models.BooleanField(
        default=False
    )
    annual_report = models.CharField(
        max_length=12,
        choices=EPA_PERMISSION_LEVEL
    )
    biennial_report = models.CharField(
        max_length=12,
        choices=EPA_PERMISSION_LEVEL
    )
    e_manifest = models.CharField(
        max_length=12,
        choices=EPA_PERMISSION_LEVEL
    )
    my_rcra_id = models.CharField(
        max_length=12,
        choices=EPA_PERMISSION_LEVEL
    )
    wiets = models.CharField(
        max_length=12,
        choices=EPA_PERMISSION_LEVEL
    )

    def __str__(self):
        return f'{self.profile.user}: {self.site}'