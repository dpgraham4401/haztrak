import pytest
from manifest.models import Signer
from manifest.serializers import ESignatureSerializer


@pytest.fixture
def e_signature_serializer(db, haztrak_json) -> ESignatureSerializer:
    """Fixture for creating an e-Manifest electronic signature serializer."""
    e_signature_serializer = ESignatureSerializer(data=haztrak_json.E_SIGNATURE.value)
    e_signature_serializer.is_valid()
    return e_signature_serializer


class TestESignatureSerializer:
    """Test suite for e-Manifest electronic signatures serialization to/from JSON."""

    @pytest.fixture(autouse=True)
    def _setup(self, haztrak_json):
        self.json = haztrak_json.E_SIGNATURE.value

    def test_e_signature_serializes(self):
        e_signature_serializer = ESignatureSerializer(data=self.json)
        assert e_signature_serializer.is_valid() is True

    def test_serializer_saves_new_signer(
        self,
        manifest_handler_factory,
        e_signature_serializer,
    ):
        e_signature_serializer.save(manifest_handler=manifest_handler_factory())
        assert Signer.objects.filter(first_name=self.json["signer"]["firstName"]).exists()

    def test_e_signature_serializer_saves_new_document(self):
        # TODO(David): implement EPA's humanReadableDocument that's part
        #  of the electronicSignaturesInfo body
        pass
