"""Service module for interacting with the e-Manifest system."""

import logging
from datetime import datetime
from typing import TYPE_CHECKING, Literal, NotRequired, TypedDict

from core.services import RcraClient, get_rcra_client
from django.db import transaction
from manifest.models import Manifest, QuickerSign
from manifest.serializers import ManifestSerializer, QuickerSignSerializer
from manifest.services.emanifest_search import EmanifestSearch
from manifest.tasks import pull_manifest, sign_manifest
from requests import RequestException

if TYPE_CHECKING:
    from django.db.models import QuerySet
    from emanifest import RcrainfoResponse

logger = logging.getLogger(__name__)


class QuickerSignData(TypedDict):
    """Type definition for the data required to sign a manifest."""

    mtn: list[str]
    site_id: str
    site_type: Literal["Generator", "Tsdf", "Transporter"]
    printed_name: str
    printed_data: datetime
    transporter_order: NotRequired[int]


class SearchManifestData(TypedDict, total=False):
    """Type definition for the data required to search for manifests."""

    site_id: str | None
    start_date: datetime | None
    end_date: datetime | None
    status: str | None
    date_type: str | None
    state_code: str | None
    site_type: str | None


class TaskResponse(TypedDict):
    """Type definition for the response returned from starting a task."""

    taskId: str


class EManifestError(Exception):
    """Base class for EManifest exceptions."""

    def __init__(self, message: str | None = None, *args):
        self.message = message
        super().__init__(*args)


class PullManifestsResult(TypedDict):
    """Type definition for the results returned from pulling manifests from RCRAInfo."""

    success: list[str]
    error: list[str]


class EManifest:
    """IO interface with the e-Manifest system."""

    def __init__(self, *, username: str | None, rcrainfo: RcraClient | None = None):
        self.username = username
        self.rcrainfo = rcrainfo or get_rcra_client(username=username)

    @property
    def is_available(self) -> bool:
        """Check if e-Manifest is available."""
        return self.rcrainfo.has_rcrainfo_credentials

    def pull(self, tracking_numbers: list[str]) -> PullManifestsResult:
        """Retrieve manifests from e-Manifest and save to database."""
        results: PullManifestsResult = {"success": [], "error": []}
        logger.info(f"pulling manifests {tracking_numbers}")
        for mtn in tracking_numbers:
            try:
                manifest_json: dict = self._retrieve_manifest(mtn)
                manifest = self._save_manifest_json_to_db(manifest_json)
                results["success"].append(manifest.mtn)
            except Exception as exc:
                logger.warning(f"error pulling manifest {mtn}: {exc}")
                results["error"].append(mtn)
        logger.info(f"pull manifests results: {results}")
        return results

    def sign(self, *, signature: QuickerSign) -> TaskResponse:
        """Validate and Launch an asynchronous task to electronically sign a manifest."""
        signature.mtn = self._filter_mtn(
            mtn=signature.mtn,
            site_id=signature.site_id,
            site_type=signature.site_type,
        )
        signature_serializer = QuickerSignSerializer(signature)
        task = sign_manifest.delay(username=self.username, **signature_serializer.data)
        return {"taskId": task.id}

    def submit_quick_signature(self, signature: dict) -> PullManifestsResult:
        """Submit a quicker signature to RCRAInfo."""
        results: PullManifestsResult = {"success": [], "error": []}
        response = self.rcrainfo.sign_manifest(**signature)
        if response.ok:
            for manifest in response.json()["manifestReports"]:
                pull_manifest.delay(
                    mtn=[manifest["manifestTrackingNumber"]],
                    username=self.username,
                )
        else:
            logger.warning(f"Error Quicker signing {response.status_code} {response.json()}")
        return results

    def save(self, manifest: dict) -> dict:
        """Save manifest to e-Manifest."""
        logger.info(f"start save manifest to rcrainfo with arguments {manifest}")
        create_resp: RcrainfoResponse = self.rcrainfo.save_manifest(manifest)
        try:
            if create_resp.ok:
                logger.info(
                    f"successfully created manifest "
                    f"{create_resp.json()['manifestTrackingNumber']} in RCRAInfo",
                )
                self.pull([create_resp.json()["manifestTrackingNumber"]])
                return create_resp.json()
            raise EManifestError(message=f"error creating manifest: {create_resp.json()}")
        except KeyError as exc:
            logger.exception(
                f"error retrieving manifestTrackingNumber from response: {create_resp.json()}",
            )
            msg = "malformed payload"
            raise EManifestError(msg) from exc

    @staticmethod
    def _filter_mtn(
        *,
        mtn: list[str],
        site_id: str,
        site_type: Literal["Generator", "Tsdf", "Transporter"],
    ) -> list[str]:
        handler_filter = Manifest.objects.filter_by_epa_id_and_site_type([site_id], site_type)
        existing_mtn = Manifest.objects.filter_existing_mtn(mtn=mtn)
        filtered_mtn = handler_filter & existing_mtn
        return [manifest.mtn for manifest in filtered_mtn]

    def _retrieve_manifest(self, mtn: str):
        """Retrieve a manifest from RCRAInfo."""
        logger.info(f"retrieving manifest from RCRAInfo {mtn}")
        response = self.rcrainfo.get_manifest(mtn)
        if response.ok:
            logger.debug(f"manifest pulled {mtn}")
            return response.json()
        logger.warning(f"error retrieving manifest {mtn}")
        raise RequestException(response.json())

    @transaction.atomic
    def _save_manifest_json_to_db(self, manifest_json: dict) -> Manifest:
        """Save manifest to Haztrak database."""
        logger.info("saving manifest to DB")
        manifest_query: QuerySet = Manifest.objects.filter(
            mtn=manifest_json["manifestTrackingNumber"],
        )
        if manifest_query.exists():
            serializer = ManifestSerializer(manifest_query.get(), data=manifest_json)
        else:
            serializer = ManifestSerializer(data=manifest_json)
        serializer.is_valid(raise_exception=True)
        logger.debug("manifest serializer is valid")
        manifest = serializer.save()
        logger.info(f"saved manifest {manifest.mtn}")
        return manifest


def get_updated_mtn(site_id: str, last_sync_date: datetime, rcra_client) -> list[str]:
    """Use the last sync date for a site to get a list of updated MTNs from RCRAInfo."""
    logger.info(f"retrieving updated MTN for site {site_id}")
    response = (
        EmanifestSearch(rcra_client)
        .add_date_type("UpdatedDate")
        .add_site_id(site_id)
        .add_start_date(last_sync_date)
        .add_end_date()
        .execute()
    )
    if response.ok:
        return response.json()
    return []


@transaction.atomic
def sync_manifests(
    *,
    site_id: str,
    last_sync_date: datetime,
    rcra_client: RcraClient,
) -> PullManifestsResult:
    """Pull manifests and update the last sync date for a site."""
    updated_mtn = get_updated_mtn(
        site_id=site_id,
        last_sync_date=last_sync_date,
        rcra_client=rcra_client,
    )
    updated_mtn = updated_mtn[:15]  # temporary limit to 15
    emanifest = EManifest(rcrainfo=rcra_client)
    results: PullManifestsResult = emanifest.pull(tracking_numbers=updated_mtn)
    return results
