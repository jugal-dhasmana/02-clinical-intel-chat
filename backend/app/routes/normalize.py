from fastapi import APIRouter
from app.schemas.normalize import NormalizeRequest, NormalizeResponse
from app.services.normalization_service import NormalizationService

router = APIRouter(prefix='/api', tags=['normalize'])
_service = NormalizationService()


@router.post('/normalize', response_model=NormalizeResponse)
async def normalize(request: NormalizeRequest) -> NormalizeResponse:
    return await _service.normalize(request)
