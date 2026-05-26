# GeoLedger Frontend

This folder contains the frontend web application for GeoLedger.

The frontend allows users to:

* Connect MetaMask wallet
* Upload geospatial datasets
* View owned datasets
* Grant access to other wallet addresses
* Download and decrypt authorized datasets
* Visualize GeoJSON data on a map
* View audit and access history

## Tech Stack

* Next.js
* React
* TypeScript
* Tailwind CSS
* Leaflet.js
* React Leaflet
* ethers.js
* Axios

## Setup

Install dependencies:

```bash
npm install
```

## Environment Variables

Create a local `.env.local` file.

Example:

```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
NEXT_PUBLIC_CHAIN_ID=80002
NEXT_PUBLIC_CHAIN_NAME=Polygon Amoy
NEXT_PUBLIC_CONTRACT_ADDRESS=
```

Do not commit `.env.local`.

## Run the Frontend

From the `frontend/` folder:

```bash
npm run dev
```

The frontend will run at:

```text
http://localhost:3000
```

## Build

```bash
npm run build
```

## Start Production Build

```bash
npm run start
```

## Important Notes

The frontend depends on:

* Backend API running on port `8000`
* MetaMask installed in the browser
* Smart contract address configured after deployment
