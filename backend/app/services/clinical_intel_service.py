from app.core.logging import get_logger
from app.schemas.clinical_intel import (
    ClinicalIntelRequest,
    ClinicalIntelResponse,
    ICDCode,
    Procedure,
    Treatment,
    ClinicalTrial,
    LiteratureReference,
    Source,
    EvidenceLevel,
    TrialPhase,
    TrialStatus,
)

logger = get_logger(__name__)

_MOCK_DB: dict[str, dict] = {
    'ittp': {
        'normalized_term': 'Immune Thrombotic Thrombocytopenic Purpura',
        'aliases': ['iTTP', 'immune TTP', 'thrombotic thrombocytopenic purpura'],
        'overview': (
            'THIS IS MY TEST RESPONSE.'
        ),
        'symptoms': [
            'Fatigue and weakness',
            'Petechiae or bruising',
            'Neurologic symptoms such as confusion or headache',
            'Abdominal pain or nausea',
            'Shortness of breath',
        ],
        'diagnosis': [
            'CBC showing thrombocytopenia and anemia',
            'Evidence of hemolysis such as elevated LDH and schistocytes',
            'Severely reduced ADAMTS13 activity, often <10%',
            'Clinical evaluation for TMA and urgent treatment need before confirmatory results if suspicion is high',
        ],
        'icd_codes': [
            ICDCode(code='M31.1', description='Thrombotic microangiopathy'),
        ],
        'procedures': [
            Procedure(name='ADAMTS13 activity test', code='85397', indication='Support diagnostic confirmation and disease characterization'),
            Procedure(name='Therapeutic plasma exchange', code='36514', indication='Core acute management procedure'),
        ],
        'treatments': [
            Treatment(name='Therapeutic plasma exchange', type='Supportive / procedural', line='Acute management', notes='A central therapy in acute episodes.'),
            Treatment(name='Corticosteroids', type='Pharmacological', line='Acute management', notes='Often used with plasma exchange.'),
            Treatment(name='Caplacizumab', type='Pharmacological', line='Adjunct', notes='Used in appropriate acute settings.'),
            Treatment(name='Rituximab', type='Pharmacological', line='Adjunct / relapse prevention', notes='Often considered in refractory or relapsing disease.'),
        ],
        'clinical_trials': [
            ClinicalTrial(nct_id='NCT03237767', title='Caplacizumab in acquired thrombotic thrombocytopenic purpura', phase=TrialPhase.PHASE_3, status=TrialStatus.COMPLETED, sponsor='Ablynx', url='https://clinicaltrials.gov/study/NCT03237767'),
        ],
        'literature': [
            LiteratureReference(title='International Society on Thrombosis and Haemostasis guidelines for thrombotic thrombocytopenic purpura', authors='Zheng XL et al.', journal='Journal of Thrombosis and Haemostasis', year=2020, doi='10.1111/jth.15006', evidence_level=EvidenceLevel.HIGH),
        ],
        'sources': [
            Source(name='ClinicalTrials.gov', url='https://clinicaltrials.gov', accessed='2026-03-29'),
        ],
        'data_considerations': [
            'Claims and EMR sources may capture different parts of the iTTP journey.',
            'ADAMTS13 testing may be sparse or delayed in some real-world datasets.',
            'Procedure and diagnosis signals may not appear on the same claims row and often need staged logic.',
        ],
    },
    'multiple myeloma': {
        'normalized_term': 'Multiple Myeloma',
        'aliases': ['MM'],
        'overview': 'Multiple myeloma is a plasma cell malignancy characterized by clonal proliferation in the bone marrow and end-organ damage in selected patients.',
        'symptoms': ['Bone pain', 'Anemia-related fatigue', 'Renal dysfunction', 'Recurrent infections'],
        'diagnosis': ['Serum and urine protein studies', 'Bone marrow evaluation', 'Imaging as clinically appropriate'],
        'icd_codes': [ICDCode(code='C90.0', description='Multiple myeloma')],
        'procedures': [Procedure(name='Bone marrow biopsy', indication='Diagnostic evaluation')],
        'treatments': [Treatment(name='Proteasome inhibitors', type='Pharmacological'), Treatment(name='Immunomodulatory agents', type='Pharmacological')],
        'clinical_trials': [],
        'literature': [],
        'sources': [],
        'data_considerations': ['Lines of therapy can be difficult to infer cleanly from claims alone.'],
    },
    'hemophilia a': {
        'normalized_term': 'Hemophilia A',
        'aliases': ['factor viii deficiency'],
        'overview': 'Hemophilia A is an inherited bleeding disorder caused by factor VIII deficiency.',
        'symptoms': ['Easy bruising', 'Joint bleeding', 'Prolonged bleeding'],
        'diagnosis': ['Factor VIII activity testing', 'Bleeding history and family history'],
        'icd_codes': [ICDCode(code='D66', description='Hereditary factor VIII deficiency')],
        'procedures': [],
        'treatments': [Treatment(name='Factor VIII replacement', type='Pharmacological / biologic')],
        'clinical_trials': [],
        'literature': [],
        'sources': [],
        'data_considerations': ['Severity classification may require lab detail not always present in claims data.'],
    },
}

_ALIAS_INDEX: dict[str, str] = {}
for _canonical, _data in _MOCK_DB.items():
    _ALIAS_INDEX[_canonical.lower()] = _canonical
    for _alias in _data.get('aliases', []):
        _ALIAS_INDEX[_alias.lower()] = _canonical


def _resolve_key(query: str) -> str | None:
    q = query.strip().lower()
    if q in _ALIAS_INDEX:
        return _ALIAS_INDEX[q]
    for key in _MOCK_DB:
        if q in key or key in q:
            return key
    return None


class ClinicalIntelService:
    async def lookup(self, request: ClinicalIntelRequest) -> ClinicalIntelResponse:
        key = _resolve_key(request.query)
        if key:
            data = _MOCK_DB[key]
            logger.info('clinical-intel | query=%r resolved=%r', request.query, key)
            return ClinicalIntelResponse(
                query=request.query,
                normalized_term=data['normalized_term'],
                aliases=data.get('aliases', []),
                overview=data['overview'],
                symptoms=data.get('symptoms', []),
                diagnosis=data.get('diagnosis', []),
                icd_codes=data.get('icd_codes', []),
                procedures=data.get('procedures', []),
                treatments=data.get('treatments', []),
                clinical_trials=data.get('clinical_trials', []),
                literature=data.get('literature', []),
                sources=data.get('sources', []),
                data_considerations=data.get('data_considerations', []),
            )

        logger.info('clinical-intel | query=%r resolved=None (fallback)', request.query)
        return ClinicalIntelResponse(
            query=request.query,
            normalized_term=request.query.title(),
            aliases=[],
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
