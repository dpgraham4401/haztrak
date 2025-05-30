"""Address model serializer."""

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rcrasite.models import Address, RcraCountries, RcraStates
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .base_serializer import SitesBaseSerializer


@extend_schema_field(OpenApiTypes.OBJECT)
class LocalityField(serializers.ChoiceField):
    """
    Locality is defined, in RCRAInfo.

    Used as an object used to describe region (state, nation)
    {
      "code": "TX",
      "name": "Texas"
    }.
    """

    def to_representation(self, obj):
        """Convert the internal value to the JSON representation of a locality."""
        return {"code": obj, "name": dict(self.choices).get(obj)}

    def to_internal_value(self, data):
        """Convert the JSON representation of a locality to the internal value."""
        try:
            return data["code"]
        except KeyError as exc:
            msg = f'"code" field is required, provided: {data}'
            raise ValidationError(msg) from exc


class AddressSerializer(SitesBaseSerializer):
    """Address model serializer for JSON representation."""

    streetNumber = serializers.CharField(
        source="street_number",
        required=False,
        allow_blank=True,
    )
    state = LocalityField(
        choices=RcraStates.choices,
        required=False,
    )
    country = LocalityField(
        choices=RcraCountries.choices,
        required=False,
    )

    class Meta:
        """Metaclass."""

        model = Address
        fields = [
            "streetNumber",
            "address1",
            "address2",
            "city",
            "state",
            "country",
            "zip",
        ]
