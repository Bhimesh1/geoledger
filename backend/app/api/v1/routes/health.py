from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "service": "GeoLedger API",
        "status": "healthy",
    }