# GeoLedger Backend

This folder contains the Python FastAPI backend for GeoLedger.

The backend handles:

* API routing
* File upload
* GeoJSON validation
* AES/RSA encryption services
* IPFS upload/download integration
* Database operations
* Blockchain interaction
* Access control workflows

## Tech Stack

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* PostgreSQL/PostGIS
* Web3.py
* Cryptography
* python-dotenv

## Folder Structure

```text
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment.

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows PowerShell

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a local `.env` file from the example file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Example variables:

```env
APP_NAME=GeoLedger
ENVIRONMENT=development
BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000
DATABASE_URL=postgresql://geoledger:geoledger@localhost:5432/geoledger
ALLOWED_ORIGINS=["http://localhost:3000","http://127.0.0.1:3000"]
```

Do not commit `.env`.

## Run the Backend

From the `backend/` folder:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/api/v1/health
```

Expected response:

```json
{
  "service": "GeoLedger API",
  "status": "healthy"
}
```

## Testing

Tests will be added under:

```text
backend/tests/
```

Run tests with:

```bash
pytest
```

## Database Setup

GeoLedger uses PostgreSQL with PostGIS.

## Local Development Database

```bash
Database: geoledger
Username: geoledger
Password: geoledger
Port: 5432
```

## Database URL

```env
DATABASE_URL=postgresql://geoledger:geoledger@localhost:5432/geoledger
```

## Run Migrations

Apply all pending migrations:

```bash
alembic upgrade head
```

## Create a New Migration After Model Changes

After changing SQLAlchemy models, create a new migration with:

```bash
alembic revision --autogenerate -m "migration message"
```

Then apply it:

```bash
alembic upgrade head
```

## Database Health Check

After running the backend, check database health at:

```text
http://127.0.0.1:8000/api/v1/database/health
```

