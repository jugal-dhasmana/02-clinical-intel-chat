from fastapi import APIRouter
from app.schemas.clinical_intel import ClinicalIntelRequest, ClinicalIntelResponse
from app.services.clinical_intel_service import ClinicalIntelService
from app.data.therapy_registry import THERAPY_DB
from pydantic import BaseModel
from app.services.ai_service import generate_therapy_response

router = APIRouter(prefix="/api", tags=["clinical-intel"])
_service = ClinicalIntelService()


@router.post("/clinical-intel", response_model=ClinicalIntelResponse)
async def clinical_intel(request: ClinicalIntelRequest) -> ClinicalIntelResponse:
    return await _service.lookup(request)


@router.get("/debug/therapies")
async def debug_therapies():
    from app.data.therapy_registry import THERAPY_DB

    return {"count": len(THERAPY_DB), "keys": list(THERAPY_DB.keys())}

class TherapyQuestionRequest(BaseModel):
    therapy_name: str
    question: str

@router.post("/clinical-intel/ask-ai")
async def ask_clinical_intel(request: TherapyQuestionRequest):

    therapy_key = request.therapy_name.strip().lower()
    therapy_data = THERAPY_DB.get(therapy_key)

    if not therapy_data:
        ai_prompt = f"""
        Therapy: {request.therapy_name}

        User Question:
        {request.question}

        This therapy is NOT curated in Clinical Intel.

        Clearly state that the response is AI-generated and not yet clinically curated.
        Provide a professional medical overview using general clinical knowledge.
        Do not fabricate citations, clinical trials, or unsupported claims.
        """

        answer = generate_therapy_response(
            question=ai_prompt,
            therapy_data={}
        )

        return {
            "therapy_name": request.therapy_name,
            "question": request.question,
            "is_curated": False,
            "answer": answer
    }

    answer = generate_therapy_response(
        question=request.question,
        therapy_data=therapy_data
    )

    return {
        "therapy_name": therapy_data.get("normalized_term", request.therapy_name),
        "question": request.question,
        "answer": answer
    }