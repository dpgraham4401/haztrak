from profile.models import RcrainfoSiteAccess
from profile.serializers import (
    ProfileSerializer,
    RcrainfoSitePermissionsSerializer,
    RcraSitePermissionSerializer,
)

import pytest


@pytest.mark.django_db
class TestTrakProfileSerializer:
    def test_serializer_includes_username(self, profile_factory, user_factory):
        my_username = "foobar1"
        user = user_factory(username=my_username)
        profile = profile_factory(user=user)
        serializer = ProfileSerializer(profile)
        assert serializer.data["user"]["username"] == my_username


class TestRcraSitePermissionSerializer:
    """Test suite is for haztrak's internal record of user's RCRAInfo site permissions."""

    @pytest.fixture(autouse=True)
    def _permissions(self, rcrainfo_site_access_factory):
        self.permissions = rcrainfo_site_access_factory()

    @pytest.fixture
    def permission_serializer(self, haztrak_json) -> RcraSitePermissionSerializer:
        return RcraSitePermissionSerializer(data=haztrak_json.SITE_PERMISSION.value)

    def test_deserializes_json(self, permission_serializer) -> None:
        assert permission_serializer.is_valid() is True

    def test_object_serializes_permission_object(self, rcrainfo_site_access_factory) -> None:
        serializer = RcraSitePermissionSerializer(self.permissions)
        assert (
            str(self.permissions.biennial_report)
            == serializer.data["permissions"]["biennialReport"]
        )


class TestRcrainfoSitePermissionSerializer:
    """
    Test suite is for Haztrak's serializer for communication with RCRAInfo site perms.

    We don't use EPaPermissionSerializer to communicate internally, so
    currently we don't serialize, only deserialize
    """

    @pytest.fixture
    def epa_permission_serializer(self, haztrak_json) -> RcrainfoSitePermissionsSerializer:
        return RcrainfoSitePermissionsSerializer(data=haztrak_json.EPA_PERMISSION.value)

    def test_deserializes_epa_permissions(
        self,
        epa_permission_serializer,
        rcrainfo_profile_factory,
        rcra_site_factory,
    ) -> None:
        if not epa_permission_serializer.is_valid():
            # if something is wrong with the serializer fixture, fail
            raise AssertionError
        rcrainfo_site_access = RcrainfoSiteAccess.objects.create(
            **epa_permission_serializer.validated_data,
            profile=rcrainfo_profile_factory(),
        )
        assert isinstance(rcrainfo_site_access, RcrainfoSiteAccess)
