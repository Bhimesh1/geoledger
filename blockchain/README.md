# GeoLedger Blockchain

This folder contains the Solidity smart contracts and Hardhat configuration for GeoLedger.

The smart contracts are responsible for:

* Registering datasets
* Storing dataset ownership
* Storing IPFS CIDs
* Storing file hashes
* Managing access permissions
* Emitting audit events

The blockchain does not store raw geospatial data or encryption keys.

## Tech Stack

* Solidity
* Hardhat
* Polygon Amoy testnet
* MetaMask
* ethers.js

## Folder Structure

```text
blockchain/
├── contracts/
│   └── GeoLedger.sol
├── scripts/
│   └── deploy.js
├── test/
│   └── GeoLedger.test.js
├── hardhat.config.js
├── package.json
├── .env.example
└── README.md
```

## Setup

Install dependencies:

```bash
npm install
```

## Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Example:

```env
AMOY_RPC_URL=https://polygon-amoy.drpc.org
PRIVATE_KEY=your_wallet_private_key_without_0x
POLYGONSCAN_API_KEY=optional_for_contract_verification
```

Never commit your real `.env` file.

Never commit:

* Private keys
* Seed phrases
* Wallet recovery phrases
* RPC secrets
* API keys

## Compile Contracts

```bash
npx hardhat compile
```

## Run Tests

```bash
npx hardhat test
```

## Deploy to Polygon Amoy

```bash
npx hardhat run scripts/deploy.js --network amoy
```

After deployment, copy the contract address into the frontend environment file:

```env
NEXT_PUBLIC_CONTRACT_ADDRESS=deployed_contract_address_here
```

## Security Notes

The smart contract should only store:

* Dataset ID
* Owner wallet address
* IPFS CID
* File hash
* Access permissions
* Blockchain events

The smart contract should not store:

* Raw geospatial files
* AES keys
* RSA private keys
* Sensitive metadata
