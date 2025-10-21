"""API endpoints for the Profile app."""

from ninja import Router

from profile.models import Profile
from profile.schemas.profile import ProfileSchema

router = Router(tags=["Profile"], by_alias=True, exclude_none=True)


@router.get("/profile", response=list[ProfileSchema])
def list_profiles(request):
    """List all profiles."""
    return Profile.objects.all()


@router.get("/profile/{user_id}", response=ProfileSchema)
def get_profile(request, user_id: str):
    """Get a profile by user UUID."""
    return Profile.objects.get_profile_by_user_id(user_id)
