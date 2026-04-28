from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List

class EvidenceLevel(str, Enum):
    HIGH = 'high'
    MODERATE = 'moderate'
    LOW = 'low'
    UNKNOWN = 'unknown'


class TrialPhase(str, Enum):
    PHASE_1 = 'Phase I'
    PHASE_2 = 'Phase II'
    PHASE_3 = 'Phase III'
    PHASE_4 = 'Phase IV'
    NOT_APPLICABLE = 'N/A'


class TrialStatus(str, Enum):
    RECRUITING = 'Recruiting'
    ACTIVE = 'Active, not recruiting'
    COMPLETED = 'Completed'
    TERMINATED = 'Terminated'
    UNKNOWN = 'Unknown'


class ICDCode(BaseModel):
    code: str = Field(..., examples=['I21.0'])
    description: str
    system: str = Field(default='ICD-10-CM')


class Procedure(BaseModel):
    name: str
    code: str | None = Field(default=None, description='CPT or SNOMED procedure code')
    indication: str | None = None


class Treatment(BaseModel):
    name: str
    type: str = Field(..., description='e.g. Pharmacological, Supportive, Lifestyle')
    line: str | None = Field(default=None, description='e.g. First-line, Escalation')
    notes: str | None = None


class ClinicalTrial(BaseModel):
    nct_id: str = Field(..., description='ClinicalTrials.gov identifier')
    title: str
    phase: TrialPhase
    status: TrialStatus
    sponsor: str | None = None
    url: str | None = None


class LiteratureReference(BaseModel):
    title: str
    authors: str
    journal: str
    year: int
    doi: str | None = None
    evidence_level: EvidenceLevel = EvidenceLevel.UNKNOWN


class Source(BaseModel):
    name: str
    url: str | None = None
    accessed: str | None = Field(default=None, description='ISO date of last access')


class ClinicalIntelRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=2,
        max_length=300,
        description='Disease name, therapy area, or drug to look up.',
        examples=['iTTP', 'multiple myeloma', 'hemophilia A'],
    )


class ClinicalIntelResponse(BaseModel):
    query: str
    is_curated: bool = True
    normalized_term: str
    aliases: List[str] = Field(default_factory=list)

    overview: str

    symptoms: List[str] = Field(default_factory=list)
    diagnosis: List[str] = Field(default_factory=list)

    icd_codes: List[ICDCode] = Field(default_factory=list)
    procedures: List[Procedure] = Field(default_factory=list)
    treatments: List[Treatment] = Field(default_factory=list)

    clinical_trials: List[ClinicalTrial] = Field(default_factory=list)
    literature: List[LiteratureReference] = Field(default_factory=list)

    sources: List[Source] = Field(default_factory=list)
    data_considerations: List[str] = Field(default_factory=list)

    disclaimer: str = Field(
        default=(
            'This information is AI-generated for educational and informational purposes only. '
            'It is not medical advice and should not be used for patient-specific decisions.'
        )
    )

    @field_validator("overview")
    def overview_not_empty(cls, v):
        if not v or len(v.strip()) < 20:
            raise ValueError("overview must be meaningful")
        return v

    @model_validator(mode="after")
    def validate_curated_minimums(self):
        if "not yet available in the current knowledge base" in self.overview.lower():
            return self

        if len(self.symptoms) < 3:
            raise ValueError("at least 3 symptoms required")
        if len(self.diagnosis) < 3:
            raise ValueError("at least 3 diagnosis points required")
        if len(self.treatments) < 2:
            raise ValueError("at least 2 treatments required")

        return self
