import pytest

from app.services import ipfs_service
from app.services.ipfs_service import (
    IPFSServiceError,
    build_ipfs_gateway_url,
    download_bytes_from_ipfs,
    upload_bytes_to_ipfs,
)


class MockUploadResponse:
    status_code = 200
    text = "OK"

    @staticmethod
    def json():
        return {
            "IpfsHash": "QmMockCid123",
            "PinSize": 128,
            "Timestamp": "2026-01-01T00:00:00Z",
        }


class MockDownloadResponse:
    status_code = 200
    text = "OK"
    content = b"encrypted file bytes"


class MockErrorResponse:
    status_code = 500
    text = "Internal Server Error"

    @staticmethod
    def json():
        return {}


def test_build_ipfs_gateway_url():
    url = build_ipfs_gateway_url("QmMockCid123")

    assert url.endswith("/QmMockCid123")


def test_upload_bytes_to_ipfs_success(monkeypatch):
    monkeypatch.setattr(ipfs_service.settings, "pinata_jwt", "test-jwt")

    def mock_post(*args, **kwargs):
        return MockUploadResponse()

    monkeypatch.setattr(ipfs_service.requests, "post", mock_post)

    result = upload_bytes_to_ipfs(
        file_bytes=b"encrypted file bytes",
        filename="roads.geojson.enc",
    )

    assert result.cid == "QmMockCid123"
    assert result.size == 128
    assert result.timestamp == "2026-01-01T00:00:00Z"


def test_upload_bytes_to_ipfs_requires_jwt(monkeypatch):
    monkeypatch.setattr(ipfs_service.settings, "pinata_jwt", "")

    with pytest.raises(IPFSServiceError, match="PINATA_JWT is not configured"):
        upload_bytes_to_ipfs(
            file_bytes=b"encrypted file bytes",
            filename="roads.geojson.enc",
        )


def test_upload_bytes_to_ipfs_handles_error(monkeypatch):
    monkeypatch.setattr(ipfs_service.settings, "pinata_jwt", "test-jwt")

    def mock_post(*args, **kwargs):
        return MockErrorResponse()

    monkeypatch.setattr(ipfs_service.requests, "post", mock_post)

    with pytest.raises(IPFSServiceError, match="IPFS upload failed"):
        upload_bytes_to_ipfs(
            file_bytes=b"encrypted file bytes",
            filename="roads.geojson.enc",
        )


def test_download_bytes_from_ipfs_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockDownloadResponse()

    monkeypatch.setattr(ipfs_service.requests, "get", mock_get)

    result = download_bytes_from_ipfs("QmMockCid123")

    assert result == b"encrypted file bytes"


def test_download_bytes_from_ipfs_requires_cid():
    with pytest.raises(IPFSServiceError, match="IPFS CID is required"):
        download_bytes_from_ipfs("")


def test_download_bytes_from_ipfs_handles_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockErrorResponse()

    monkeypatch.setattr(ipfs_service.requests, "get", mock_get)

    with pytest.raises(IPFSServiceError, match="IPFS download failed"):
        download_bytes_from_ipfs("QmMockCid123")