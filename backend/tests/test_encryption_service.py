import base64

import pytest

from app.services.encryption_service import (
    calculate_sha256,
    decrypt_aes_key_with_rsa_private_key,
    decrypt_bytes,
    encrypt_aes_key_with_rsa_public_key,
    encrypt_file_bytes,
    generate_aes_key,
    generate_rsa_key_pair,
)


def test_generate_aes_key_has_correct_length():
    aes_key = generate_aes_key()

    assert isinstance(aes_key, bytes)
    assert len(aes_key) == 32


def test_encrypt_and_decrypt_bytes_successfully():
    original_data = b'{"type":"FeatureCollection","features":[]}'

    encrypted_payload, aes_key = encrypt_file_bytes(original_data)

    decrypted_data = decrypt_bytes(
        encrypted_payload.nonce_b64,
        encrypted_payload.ciphertext_b64,
        aes_key,
    )

    assert decrypted_data == original_data
    assert encrypted_payload.ciphertext_b64 != original_data.decode("utf-8")


def test_encrypted_payload_is_base64_encoded():
    original_data = b"sample geospatial data"

    encrypted_payload, _ = encrypt_file_bytes(original_data)

    base64.b64decode(encrypted_payload.nonce_b64)
    base64.b64decode(encrypted_payload.ciphertext_b64)


def test_sha256_hash_is_consistent():
    data = b"geoledger"

    first_hash = calculate_sha256(data)
    second_hash = calculate_sha256(data)

    assert first_hash == second_hash
    assert len(first_hash) == 64


def test_generate_rsa_key_pair_contains_pem_headers():
    key_pair = generate_rsa_key_pair()

    assert "BEGIN PRIVATE KEY" in key_pair.private_key_pem
    assert "BEGIN PUBLIC KEY" in key_pair.public_key_pem


def test_encrypt_and_decrypt_aes_key_with_rsa():
    aes_key = generate_aes_key()
    key_pair = generate_rsa_key_pair()

    encrypted_aes_key = encrypt_aes_key_with_rsa_public_key(
        aes_key,
        key_pair.public_key_pem,
    )

    decrypted_aes_key = decrypt_aes_key_with_rsa_private_key(
        encrypted_aes_key,
        key_pair.private_key_pem,
    )

    assert decrypted_aes_key == aes_key


def test_invalid_aes_key_length_raises_error():
    invalid_key = b"too-short"
    data = b"sample"

    with pytest.raises(ValueError, match="AES key must be 32 bytes"):
        encrypt_file_bytes(data, invalid_key)