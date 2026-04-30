from app.core.logging import get_logger
from app.data.therapy_registry import THERAPY_DB, resolve_therapy_key, suggest_therapies
from app.schemas.clinical_intel import (
    ClinicalIntelRequest,
    ClinicalIntelResponse,
)

logger = get_logger(__name__)


class ClinicalIntelService:
    async def lookup(self, request: ClinicalIntelRequest) -> ClinicalIntelResponse:
        key = resolve_therapy_key(request.query)

        if key:
            data = THERAPY_DB[key]

            logger.info("clinical-intel | query=%r resolved=%r", request.query, key)

            return ClinicalIntelResponse(
                query=request.query,
                is_curated=True,
                normalized_term=data["normalized_term"],
                aliases=data.get("aliases", []),
                suggestions=[],
                overview=data["overview"],
                symptoms=data.get("symptoms", []),
                diagnosis=data.get("diagnosis", []),
                icd_codes=data.get("icd_codes", []),
                procedures=data.get("procedures", []),
                treatments=data.get("treatments", []),
                clinical_trials=data.get("clinical_trials", []),
                literature=data.get("literature", []),
                sources=data.get("sources", []),
                data_considerations=data.get("data_considerations", []),
            )

        logger.info("clinical-intel | query=%r resolved=None (fallback)", request.query)

        suggestions = suggest_therapies(request.query)

        return ClinicalIntelResponse(
            query=request.query,
            is_curated=False,
            normalized_term=request.query.title(),
            aliases=[],
            suggestions=suggestions,
            overview=(
                f"Structured clinical intelligence data for '{request.query}' is not yet available in the current knowledge base."
            ),
            symptoms=[],
            diagnosis=[],
            icd_codes=[],
            procedures=[],
            treatments=[],
            clinical_trials=[],
            literature=[],
            sources=[],
            data_considerations=[],
        )
