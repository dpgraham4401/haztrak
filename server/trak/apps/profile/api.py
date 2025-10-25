"""API endpoints for the Profile app."""

from django.http import HttpRequest
from ninja import Router
from ninja.errors import AuthenticationError

from trak.apps.profile.models import Profile, RcrainfoProfile
from trak.apps.profile.schemas.profile import ProfileSchema
from trak.apps.profile.schemas.rcrainfo_profile import RcrainfoProfileSchema

router = Router(tags=["Profile"], by_alias=True, exclude_none=True)


@router.get("/profile", response=list[ProfileSchema])
def list_profiles(request):
    """List all profiles."""
    return Profile.objects.all()


@router.get("/profile/me", response=ProfileSchema)
def get_my_profile(request: HttpRequest):
    """Get the profile of the currently authenticated user."""
    user = request.user
    if user.is_anonymous:
        raise AuthenticationError(message="Authentication required to access this endpoint.")
    return Profile.objects.get_profile_by_user(user)


@router.get("/profile/{user_id}", response=ProfileSchema)
def get_profile(request, user_id: str):
    """Get a profile by user UUID."""
    return Profile.objects.get_profile_by_user_id(user_id)


@router.get("/profile/rcrainfo/me", response=RcrainfoProfileSchema)
def get_my_rcrainfo_profile(request):
    """Get a RCRAInfo profile of the currently authenticated user."""
    user = request.user
    if user.is_anonymous:
        raise AuthenticationError(message="Authentication required to access this endpoint.")
    return RcrainfoProfile.objects.get_by_trak_user_id(user.id)


@router.get("/profile/rcrainfo/{user_id}", response=RcrainfoProfileSchema)
def get_rcrainfo_profile(request, user_id: str):
    """Get a RCRAInfo profile by user UUID."""
    return RcrainfoProfile.objects.get_by_trak_user_id(user_id)
