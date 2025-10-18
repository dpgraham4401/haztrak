"""Handler Schema serializer."""

from pydantic import BaseModel, ConfigDict, Field
from rcrasite.schemas import AddressSchema

# class RcraSiteSerializer(SitesBaseSerializer):
#     """RcraSite model serializer for JSON marshalling/unmarshalling."""
#
#     epaSiteId = serializers.CharField(
#         source="epa_id",
#     )
#     siteType = serializers.ChoiceField(
#         source="site_type",
#         allow_null=True,
#         required=False,
#         choices=RcraSiteType.choices,
#     )
#     modified = serializers.BooleanField(
#         allow_null=True,
#         default=False,
#     )
#     # name
#     mailingAddress = AddressSerializer(
#         source="mail_address",
#     )
#     siteAddress = AddressSerializer(
#         source="site_address",
#     )
#     contact = ContactSerializer()
#     emergencyPhone = RcraPhoneSerializer(
#         source="emergency_phone",
#         allow_null=True,
#         default=None,
#     )
#     # paperSignatureInfo
#     registered = serializers.BooleanField(
#         allow_null=True,
#         default=False,
#     )
#     limitedEsign = serializers.BooleanField(
#         source="limited_esign",
#         allow_null=True,
#         default=False,
#     )
#     canEsign = serializers.BooleanField(
#         source="can_esign",
#         allow_null=True,
#         default=False,
#     )
#     hasRegisteredEmanifestUser = serializers.BooleanField(
#         source="registered_emanifest_user",
#         allow_null=True,
#         default=False,
#     )
#     gisPrimary = serializers.BooleanField(
#         source="gis_primary",
#         allow_null=True,
#         default=False,
#     )
#
#     def update(self, instance, validated_data):
#         """Update an existing RcraSite instance."""
#         return self.Meta.model.objects.save(instance, **validated_data)
#
#     def create(self, validated_data):
#         """Create a new RcraSite instance."""
#         return self.Meta.model.objects.save(None, **validated_data)
#
#     class Meta:
#         """Metaclass."""
#
#         model = RcraSite
#         fields = [
#             "epaSiteId",
#             "siteType",
#             "modified",
#             "name",
#             "siteAddress",
#             "mailingAddress",
#             "contact",
#             "emergencyPhone",
#             "registered",
#             "limitedEsign",
#             "canEsign",
#             "hasRegisteredEmanifestUser",
#             "gisPrimary",
#         ]


class HandlerSchema(BaseModel):
    """Schema for serializering and deserializing handler information."""

    epa_id: str = Field(..., alias="epaSiteId")
    site_type: str | None = Field(None, alias="siteType")
    modified: bool = Field(False)
    name: str = Field(..., description="The name of the handler.")
    site_address: AddressSchema | None
    mail_address: AddressSchema | None
    # contact:
    # emergency_phone:
    limited_esign: bool = Field(False)
    can_esign: bool = Field(False)
    registered_emanifest_user: bool = Field(False)
    gis_primary: bool = Field(False)

    model_config = ConfigDict(from_attributes=True)
