import base64
import hashlib
import os
from dataclasses import dataclass

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


AES_KEY_SIZE_BYTES = 32
AES_NONCE_SIZE_BYTES = 12
RSA_KEY_SIZE_BITS = 2048


@dataclass(frozen=True)
class EncryptedPayload:
    nonce_b64: str
    ciphertext_b64: str
    sha256_hash: str


@dataclass(frozen=True)
class RSAKeyPair:
    private_key_pem: str
    public_key_pem: str


def generate_aes_key() -> bytes:
    """
    Generate a random AES-256 key.

    Returns:
        32-byte AES key.
    """
    return os.urandom(AES_KEY_SIZE_BYTES)


def encrypt_bytes(data: bytes, aes_key: bytes) -> EncryptedPayload:
    """
    Encrypt bytes using AES-256-GCM.

    AES-GCM provides confidentiality and integrity protection.
    """
    _validate_aes_key(aes_key)

    nonce = os.urandom(AES_NONCE_SIZE_BYTES)
    aesgcm = AESGCM(aes_key)

    ciphertext = aesgcm.encrypt(nonce, data, associated_data=None)
    encrypted_blob = nonce + ciphertext

    return EncryptedPayload(
        nonce_b64=base64.b64encode(nonce).decode("utf-8"),
        ciphertext_b64=base64.b64encode(ciphertext).decode("utf-8"),
        sha256_hash=calculate_sha256(encrypted_blob),
    )


def decrypt_bytes(nonce_b64: str, ciphertext_b64: str, aes_key: bytes) -> bytes:
    """
    Decrypt AES-256-GCM encrypted bytes.
    """
    _validate_aes_key(aes_key)

    nonce = base64.b64decode(nonce_b64)
    ciphertext = base64.b64decode(ciphertext_b64)

    aesgcm = AESGCM(aes_key)

    return aesgcm.decrypt(nonce, ciphertext, associated_data=None)


def encrypt_file_bytes(file_bytes: bytes, aes_key: bytes | None = None) -> tuple[EncryptedPayload, bytes]:
    """
    Encrypt file bytes.

    If no AES key is provided, a new AES-256 key is generated.

    Returns:
        encrypted payload and AES key.
    """
    key = aes_key or generate_aes_key()
    encrypted_payload = encrypt_bytes(file_bytes, key)

    return encrypted_payload, key


def calculate_sha256(data: bytes) -> str:
    """
    Calculate SHA-256 hash for bytes.
    """
    return hashlib.sha256(data).hexdigest()


def generate_rsa_key_pair() -> RSAKeyPair:
    """
    Generate a 2048-bit RSA private/public key pair.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=RSA_KEY_SIZE_BITS,
    )

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")

    public_key_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("utf-8")

    return RSAKeyPair(
        private_key_pem=private_key_pem,
        public_key_pem=public_key_pem,
    )


def encrypt_aes_key_with_rsa_public_key(aes_key: bytes, public_key_pem: str) -> str:
    """
    Encrypt AES key with recipient RSA public key.

    Returns:
        Base64-encoded encrypted AES key.
    """
    _validate_aes_key(aes_key)

    public_key = serialization.load_pem_public_key(public_key_pem.encode("utf-8"))

    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return base64.b64encode(encrypted_key).decode("utf-8")


def decrypt_aes_key_with_rsa_private_key(encrypted_aes_key_b64: str, private_key_pem: str) -> bytes:
    """
    Decrypt AES key using recipient RSA private key.
    """
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode("utf-8"),
        password=None,
    )

    encrypted_key = base64.b64decode(encrypted_aes_key_b64)

    decrypted_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    _validate_aes_key(decrypted_key)

    return decrypted_key


def _validate_aes_key(aes_key: bytes) -> None:
    if len(aes_key) != AES_KEY_SIZE_BYTES:
        raise ValueError("AES key must be 32 bytes for AES-256")