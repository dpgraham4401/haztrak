"""Serializers for Handler and Transporter models."""

from manifest.models import Handler, ManifestPhone, Transporter
from rcrasite.serializers import RcraSiteSerializer
from rest_framework import serializers

from .signatures import ESignatureSerializer, PaperSignatureSerializer


class ManifestPhoneSerializer(serializers.ModelSerializer):
    """Serializer for phone numbers on manifest."""

    number = serializers.CharField(
        required=True,
    )
    extension = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    class Meta:
        """Metaclass."""

        model = ManifestPhone
        fields = ["number", "extension"]


class HandlerSerializer(RcraSiteSerializer):
    """Serializer for RcraSite on manifest."""

    rcra_site = RcraSiteSerializer()
    electronicSignaturesInfo = ESignatureSerializer(
        source="e_signatures",
        many=True,
        required=False,
    )
    paperSignatureInfo = PaperSignatureSerializer(
        source="paper_signature",
        required=False,
    )
    emergencyPhone = ManifestPhoneSerializer(
        source="emergency_phone",
        required=False,
    )
    signed = serializers.ReadOnlyField()

    def update(self, instance, validated_data: dict):
        """Update an existing handler."""
        return self.Meta.model.objects.save(instance, **validated_data)

    def create(self, validated_data: dict):
        """Create a new handler."""
        return self.Meta.model.objects.save(None, **validated_data)

    def to_representation(self, instance):
        """Convert model instance to JSON."""
        representation = super().to_representation(instance)
        handler_rep = representation.pop("rcra_site")
        for key in handler_rep:
            representation[key] = handler_rep[key]
        return representation

    def to_internal_value(self, data: dict):
        """Convert JSON data to internal value."""
        instance = {}
        if "electronicSignaturesInfo" in data:
            instance["electronicSignaturesInfo"] = data.pop("electronicSignaturesInfo")
        if "emergencyPhone" in data:
            instance["emergencyPhone"] = data.pop("emergencyPhone")
        if "paperSignatureInfo" in data:
            instance["paperSignatureInfo"] = data.pop("paperSignatureInfo")
        instance["rcra_site"] = data
        if "order" in instance["rcra_site"]:
            instance["order"] = instance["rcra_site"]["order"]
        return super().to_internal_value(instance)

    class Meta:
        """Metaclass."""

        model = Handler
        fields = [
            "rcra_site",
            "electronicSignaturesInfo",
            "paperSignatureInfo",
            "emergencyPhone",
            "signed",
        ]


class TransporterSerializer(HandlerSerializer):
    """Transporter model serializer for JSON marshalling/unmarshalling."""

    class Meta:
        """Metaclass."""

        model = Transporter
        fields = [
            "rcra_site",
            "order",
            "paperSignatureInfo",
            "electronicSignaturesInfo",
            "signed",
        ]
