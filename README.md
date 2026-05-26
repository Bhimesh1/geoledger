
# GeoLedger

GeoLedger is a secure blockchain-based geospatial data sharing platform.

It uses:

- Python FastAPI for the backend
- React / Next.js for the frontend
- IPFS for encrypted file storage
- AES-256 for geospatial file encryption
- RSA for secure AES key sharing
- Solidity smart contracts for dataset ownership, permissions, and audit logs
- Polygon Amoy testnet for the student MVP
- PostgreSQL + PostGIS for geospatial metadata

## Project Structure

```text
geoledger/
├── backend/
├── frontend/
├── blockchain/
└── docs/
```
## MVP Goal

The MVP allows users to upload an encrypted GeoJSON file, store it on IPFS, register its hash and ownership on blockchain, grant access to another user, and allow authorized users to decrypt and view the data on a map.



# Phase 1 checklist

By the end of Phase 1, you should have:

```text
GeoLedger root folder created
FastAPI backend running
Next.js frontend running
Hardhat blockchain workspace created
Docs folder created
Environment example files created
Gitignore configured
Recommended build order after Phase 1
```

We’ll build GeoLedger in this order:
```
Phase 1: Project setup and folder structure
Phase 2: Smart contract for dataset registry and access control
Phase 3: FastAPI backend database models
Phase 4: AES/RSA encryption service
Phase 5: IPFS upload/download service
Phase 6: Backend dataset upload API
Phase 7: MetaMask wallet authentication
Phase 8: Frontend dashboard
Phase 9: GeoJSON map visualization
Phase 10: Access sharing and decryption workflow
Phase 11: Audit logs and final documentation
```



