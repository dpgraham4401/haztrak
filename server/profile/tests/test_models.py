import pytest
from django.contrib.auth.models import AbstractUser

from profile.models import Profile, RcrainfoProfile


@pytest.mark.django_db
class TestRcrainfoProfileModel:
    """Test related to the RcrainfoProfile model and its API."""

    @pytest.fixture
    def user_profile_rcra_profile_factory(self, rcrainfo_profile_factory, profile_factory):
        """Helper to create a user, profile, and rcrainfo profile together."""

        def _factory(**kwargs) -> tuple[AbstractUser, Profile, RcrainfoProfile]:
            rcrainfo_profile = rcrainfo_profile_factory(**kwargs)
            profile = profile_factory(rcrainfo_profile=rcrainfo_profile)
            return profile.user, profile, rcrainfo_profile

        return _factory

    def test_rcra_profile_factory(self, rcrainfo_profile_factory):
        """Simply check the model saves given our factory's defaults."""
        rcra_profile = rcrainfo_profile_factory()
        assert isinstance(rcra_profile, RcrainfoProfile)

    @pytest.mark.parametrize("rcra_api_id", ["id", None])
    @pytest.mark.parametrize("rcra_api_key", ["key", None])
    def test_rcra_profile_is_not_api_user_if_one_missing(
        self,
        rcrainfo_profile_factory,
        rcra_api_id,
        rcra_api_key,
    ):
        """If any of the three are None, the user should not be considered an API user."""
        # Arrange
        expected = True
        if rcra_api_id is None or rcra_api_key is None:
            expected = False
        rcra_profile = rcrainfo_profile_factory(rcra_api_id=rcra_api_id, rcra_api_key=rcra_api_key)
        # Act
        api_user = rcra_profile.has_rcrainfo_api_id_key
        # Assert
        assert api_user is expected

    def test_get_by_trak_username_returns_a_rcrainfo_profile(
        self, user_profile_rcra_profile_factory
    ):
        user, _, _ = user_profile_rcra_profile_factory()
        returned_profile = RcrainfoProfile.objects.get_by_trak_username(user.username)
        assert isinstance(returned_profile, RcrainfoProfile)

    def test_get_rcrainfo_profile_by_trak_user_id(self, user_profile_rcra_profile_factory):
        """We can retrieve a RcrainfoProfile by the related Trak user ID."""
        user, _, _ = user_profile_rcra_profile_factory()
        returned_profile = RcrainfoProfile.objects.get_by_trak_user_id(user.id)
        assert isinstance(returned_profile, RcrainfoProfile)

    def test_only_executes_one_query(
        self, user_profile_rcra_profile_factory, django_assert_num_queries
    ):
        """We can retrieve a RcrainfoProfile by the related Trak user ID."""
        user, _, _ = user_profile_rcra_profile_factory()
        with django_assert_num_queries(1):
            _ = RcrainfoProfile.objects.get_by_trak_user_id(user.id)


class TestProfileModel:
    def test_haztrak_profile_factory(self, profile_factory):
        profile = profile_factory()
        assert isinstance(profile, Profile)

    def test_get_profile_by_user(self, profile_factory, user_factory):
        user = user_factory()
        saved_profile = profile_factory(user=user)
        profile = Profile.objects.get_profile_by_user(user)
        assert profile == saved_profile

    def test_get_profile_by_user_id(self, profile_factory, user_factory):
        user = user_factory()
        saved_profile = profile_factory(user=user)
        profile = Profile.objects.get_profile_by_user_id(user.id)
        assert profile == saved_profile

    def test_by_user_id_raises_error_if_not_found(self, profile_factory, user_factory):
        """Get profile by user ID raises Profile.DoesNotExist if not found."""
        with pytest.raises(Profile.DoesNotExist):
            Profile.objects.get_profile_by_user_id(9999)
