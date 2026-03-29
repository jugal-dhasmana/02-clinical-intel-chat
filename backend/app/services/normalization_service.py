from app.core.logging import get_logger
from app.schemas.normalize import (
    NormalizeRequest,
    NormalizeResponse,
    NormalizedConcept,
    TerminologySystem,
)

logger = get_logger(__name__)

_MOCK_CONCEPTS: dict[str, list[dict]] = {
    'ittp': [
        {'code': 'M31.1', 'display': 'Thrombotic microangiopathy', 'system': TerminologySystem.ICD10, 'confidence': 0.88},
        {'code': 'immune thrombotic thrombocytopenic purpura', 'display': 'Immune thrombotic thrombocytopenic purpura', 'system': TerminologySystem.UNKNOWN, 'confidence': 0.9},
    ],
    'multiple myeloma': [
        {'code': 'C90.0', 'display': 'Multiple myeloma', 'system': TerminologySystem.ICD10, 'confidence': 0.98},
    ],
    'hemophilia a': [
        {'code': 'D66', 'display': 'Hereditary factor VIII deficiency', 'system': TerminologySystem.ICD10, 'confidence': 0.99},
    ],
}


class NormalizationService:
    async def normalize(self, request: NormalizeRequest) -> NormalizeResponse:
        key = request.text.strip().lower()
        raw_concepts = _MOCK_CONCEPTS.get(key, [
            {
                'code': 'UNKNOWN',
                'display': request.text,
                'system': TerminologySystem.UNKNOWN,
                'confidence': 0.0,
            }
        ])

        if request.preferred_system:
            filtered = [c for c in raw_concepts if c['system'] == request.preferred_system]
            if filtered:
                raw_concepts = filtered

        concepts = [NormalizedConcept(**c) for c in raw_concepts]
        matched = any(c.system != TerminologySystem.UNKNOWN for c in concepts)
        logger.info('normalize | text=%r matched=%s concepts=%d', request.text, matched, len(concepts))
        return NormalizeResponse(original_text=request.text, concepts=concepts, matched=matched)
