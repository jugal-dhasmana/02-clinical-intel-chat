from fastapi import APIRouter
from app.schemas.health import HealthResponse
from app.services.health_service import HealthService

router = APIRouter(tags=['health'])
_service = HealthService()


@router.get('/health', response_model=HealthResponse)
async def health() -> HealthResponse:
    return _service.get_health()
