from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes.database import router as database_router
from app.api.v1.routes.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title="GeoLedger API",
    description="Secure geospatial data sharing platform using FastAPI, IPFS, AES/RSA encryption, and blockchain.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(database_router, prefix="/api/v1", tags=["Database"])


@app.get("/")
def root():
    return {
        "message": "Welcome to GeoLedger API",
        "status": "running",
    }