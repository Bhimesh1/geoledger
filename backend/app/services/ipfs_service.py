from dataclasses import dataclass

import requests

from app.core.config import settings


@dataclass(frozen=True)
class IPFSUploadResult:
    cid: str
    size: int
    timestamp: str | None = None


class IPFSServiceError(Exception):
    """Raised when IPFS upload or download fails."""


def upload_bytes_to_ipfs(
    file_bytes: bytes,
    filename: str,
    content_type: str = "application/octet-stream",
) -> IPFSUploadResult:
    """
    Upload bytes to IPFS using Pinata.

    Returns:
        IPFSUploadResult containing the IPFS CID.
    """
    if not settings.pinata_jwt or settings.pinata_jwt == "your_pinata_jwt_here":
        raise IPFSServiceError("PINATA_JWT is not configured")

    files = {
        "file": (
            filename,
            file_bytes,
            content_type,
        )
    }

    headers = {
        "Authorization": f"Bearer {settings.pinata_jwt}",
    }

    response = requests.post(
        settings.pinata_upload_url,
        files=files,
        headers=headers,
        timeout=60,
    )

    if response.status_code >= 400:
        raise IPFSServiceError(
            f"IPFS upload failed with status {response.status_code}: {response.text}"
        )

    data = response.json()

    cid = data.get("IpfsHash")
    size = data.get("PinSize")
    timestamp = data.get("Timestamp")

    if not cid:
        raise IPFSServiceError("IPFS upload response did not include IpfsHash")

    return IPFSUploadResult(
        cid=cid,
        size=int(size or len(file_bytes)),
        timestamp=timestamp,
    )


def download_bytes_from_ipfs(cid: str) -> bytes:
    """
    Download bytes from IPFS using the configured gateway.
    """
    if not cid:
        raise IPFSServiceError("IPFS CID is required")

    gateway_url = settings.pinata_gateway_url.rstrip("/")
    url = f"{gateway_url}/{cid}"

    response = requests.get(
        url,
        timeout=60,
    )

    if response.status_code >= 400:
        raise IPFSServiceError(
            f"IPFS download failed with status {response.status_code}: {response.text}"
        )

    return response.content


def build_ipfs_gateway_url(cid: str) -> str:
    """
    Build a public gateway URL for an IPFS CID.
    """
    if not cid:
        raise IPFSServiceError("IPFS CID is required")

    gateway_url = settings.pinata_gateway_url.rstrip("/")

    return f"{gateway_url}/{cid}"