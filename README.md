# GeoLedger

GeoLedger is a secure blockchain-based geospatial data sharing platform.

It allows users and organizations to upload, encrypt, share, verify, and visualize geospatial datasets with strong access control and tamper-resistant auditability.

The platform is designed for smart city systems, university research, government data exchange, infrastructure planning, and secure geospatial collaboration.

## Overview

Geospatial datasets can contain sensitive information about infrastructure, transportation, utilities, land use, environmental risks, and urban planning. GeoLedger protects these datasets by combining encryption, decentralized storage, blockchain-based verification, and controlled access sharing.

GeoLedger does not store raw geospatial data on the blockchain. Instead, files are encrypted before storage, uploaded to IPFS, and only cryptographic references such as file hashes, dataset ownership, and access permissions are recorded on-chain.

## Key Features

- Wallet-based authentication using MetaMask
- Secure geospatial file upload
- AES-256 encryption for geospatial datasets
- RSA encryption for secure AES key sharing
- Encrypted file storage using IPFS
- Dataset ownership registration on blockchain
- Smart contract-based access permissions
- Tamper-resistant audit logs
- File integrity verification using blockchain hashes
- GeoJSON visualization on an interactive map
- PostgreSQL/PostGIS metadata storage

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React / Next.js |
| Map Visualization | Leaflet.js |
| Backend | Python FastAPI |
| Database | PostgreSQL + PostGIS |
| Storage | IPFS |
| Blockchain | Polygon Amoy testnet |
| Smart Contracts | Solidity |
| Blockchain Development | Hardhat |
| Wallet | MetaMask |
| Encryption | AES-256 + RSA |

## Project Structure

```text
geoledger/
├── backend/        # FastAPI backend service
├── frontend/       # Next.js frontend application
├── blockchain/     # Solidity smart contracts and Hardhat setup
├── docs/           # Project documentation
├── .gitignore
└── README.md
```

## How the System Works
```
User uploads GeoJSON file
        ↓
Backend validates file
        ↓
File is encrypted using AES-256
        ↓
Encrypted file is uploaded to IPFS
        ↓
IPFS CID and file hash are generated
        ↓
Dataset ownership and hash are stored on blockchain
        ↓
Authorized users receive encrypted access keys
        ↓
Users decrypt and visualize the dataset on a map
```

## Running the Project

GeoLedger contains three main applications:

1. Backend API
2. Frontend web application
3. Blockchain smart contract workspace

Each part has its own setup instructions.

### Backend

See:

`backend/README.md`


### Frontend

See:

`frontend/README.md`


### Blockchain

See:

`blockchain/README.md`


## Environment Variables

Each application uses its own environment file.

Use the example files as templates:

```
backend/.env.example
blockchain/.env.example
frontend/.env.example
```


Never commit real `.env` files or private keys.


## Documentation

Additional documentation is available in the `docs/` folder.

File	Purpose
docs/architecture.md	System architecture and design
docs/api.md	Backend API documentation
docs/smart-contracts.md	Smart contract design
docs/setup.md	Full local setup guide
docs/development-roadmap.md	Development phases and build plan
Security Notes

GeoLedger is designed with security as a core requirement.

Important principles:

Raw geospatial files are never stored on-chain.
Only encrypted files are uploaded to IPFS.
AES keys are never shared in plain text.
Access permissions are recorded using smart contracts.
File hashes are stored on-chain for integrity verification.
Real private keys and secrets must never be committed to GitHub.



## Documentation

Additional documentation is available in the `docs/` folder.

| File                          | Purpose                           |
| ----------------------------- | --------------------------------- |
| `docs/architecture.md`        | System architecture and design    |
| `docs/api.md`                 | Backend API documentation         |
| `docs/smart-contracts.md`     | Smart contract design             |
| `docs/setup.md`               | Full local setup guide            |
| `docs/development-roadmap.md` | Development phases and build plan |

## Security Notes

GeoLedger is designed with security as a core requirement.

Important principles:

| Principle                  | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| No raw files on-chain      | Raw geospatial files are never stored on-chain.                  |
| Encrypted IPFS storage     | Only encrypted files are uploaded to IPFS.                       |
| Protected AES keys         | AES keys are never shared in plain text.                         |
| Smart contract permissions | Access permissions are recorded using smart contracts.           |
| Integrity verification     | File hashes are stored on-chain for integrity verification.      |
| Secret protection          | Real private keys and secrets must never be committed to GitHub. |

## License

This project is currently developed as a student research and prototype project.




