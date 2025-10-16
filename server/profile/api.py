"""API endpoints for the Profile app."""

from ninja import Router

from profile.models import Profile
from profile.schemas.profile import ProfileSchema

router = Router(tags=["Profile"], by_alias=True)


@router.get("/profile", response=list[ProfileSchema])
def list_profiles(request):
    """List all profiles."""
    return Profile.objects.all()
