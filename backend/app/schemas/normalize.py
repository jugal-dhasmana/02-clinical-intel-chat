from enum import Enum
from pydantic import BaseModel, Field


class TerminologySystem(str, Enum):
    ICD10 = 'ICD-10-CM'
    SNOMED = 'SNOMED-CT'
    LOINC = 'LOINC'
    RXNORM = 'RxNorm'
    UNKNOWN = 'UNKNOWN'


class NormalizeRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=200)
    preferred_system: TerminologySystem | None = None


class NormalizedConcept(BaseModel):
    code: str
    display: str
    system: TerminologySystem
    confidence: float


class NormalizeResponse(BaseModel):
    original_text: str
    concepts: list[NormalizedConcept]
    matched: bool
