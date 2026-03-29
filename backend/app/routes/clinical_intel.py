from fastapi import APIRouter
from app.schemas.clinical_intel import ClinicalIntelRequest, ClinicalIntelResponse
from app.services.clinical_intel_service import ClinicalIntelService

router = APIRouter(prefix='/api', tags=['clinical-intel'])
_service = ClinicalIntelService()


@router.post('/clinical-intel', response_model=ClinicalIntelResponse)
async def clinical_intel(request: ClinicalIntelRequest) -> ClinicalIntelResponse:
    return await _service.lookup(request)
