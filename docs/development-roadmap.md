# GeoLedger Development Roadmap

This document tracks the development phases, milestones, and commit checkpoints for GeoLedger.

The root README should remain project-facing and should not contain phase-by-phase development history.

## Phase 1: Project Foundation

**Goal:**

Create the initial monorepo structure with backend, frontend, blockchain, and documentation folders.

**Expected commit:**

```text
chore: initialize GeoLedger project structure
```

## Phase 2: Smart Contract Foundation

**Goal:**

Create the first version of the GeoLedger smart contract for dataset registration and access control.

**Expected commits:**

```text
feat: add GeoLedger smart contract
test: add smart contract tests
chore: configure Hardhat for Polygon Amoy
```

## Phase 3: Backend Database Foundation

**Goal:**

Create database connection, SQLAlchemy models, and migration setup.

**Expected commits:**

```text
feat: add backend database configuration
feat: add dataset and user models
```

## Phase 4: Encryption Services

**Goal:**

Add AES encryption for files and RSA encryption for key sharing.

**Expected commits:**

```text
feat: add AES encryption service
feat: add RSA key sharing service
test: add encryption service tests
```

## Phase 5: IPFS Integration

**Goal:**

Add IPFS upload and download service for encrypted files.

**Expected commit:**

```text
feat: add IPFS storage service
```

## Phase 6: Dataset Upload API

**Goal:**

Add API endpoints for uploading, encrypting, storing, and registering geospatial datasets.

**Expected commit:**

```text
feat: add dataset upload API
```

## Phase 7: Wallet Authentication

**Goal:**

Add MetaMask wallet authentication using signed messages.

**Expected commit:**

```text
feat: add wallet authentication
```

## Phase 8: Frontend Dashboard

**Goal:**

Create the frontend dashboard layout and connect it to the backend.

**Expected commit:**

```text
feat: add frontend dashboard
```

## Phase 9: GeoJSON Map Visualization

**Goal:**

Display decrypted GeoJSON datasets on an interactive map.

**Expected commit:**

```text
feat: add GeoJSON map visualization
```

## Phase 10: Access Sharing Workflow

**Goal:**

Allow dataset owners to grant and revoke access for other users.

**Expected commit:**

```text
feat: add dataset access sharing
```

## Phase 11: Audit Logs and Final Documentation

**Goal:**

Add audit log views and complete documentation.

**Expected commits:**

```text
feat: add audit log dashboard
docs: complete project documentation
```
