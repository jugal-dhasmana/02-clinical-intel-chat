from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, Field


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
    normalized_term: str
    aliases: list[str] = Field(default_factory=list)
    overview: str
    symptoms: list[str] = Field(default_factory=list)
    diagnosis: list[str] = Field(default_factory=list)
    icd_codes: list[ICDCode] = Field(default_factory=list)
    procedures: list[Procedure] = Field(default_factory=list)
    treatments: list[Treatment] = Field(default_factory=list)
    clinical_trials: list[ClinicalTrial] = Field(default_factory=list)
    literature: list[LiteratureReference] = Field(default_factory=list)
    sources: list[Source] = Field(default_factory=list)
    data_considerations: list[str] = Field(default_factory=list)
    disclaimer: str = Field(
        default=(
            'This information is AI-generated for educational and informational purposes only. '
            'It is not medical advice and should not be used for patient-specific decisions.'
        )
    )
