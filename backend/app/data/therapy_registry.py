import difflib
from app.data.therapies.gi import THERAPIES_GI
from app.data.therapies.liver import THERAPIES_LIVER
from app.data.therapies.heme_rare import THERAPIES_HEME_RARE
from app.data.therapies.derm_rheum import THERAPIES_DERM_RHEUM
from app.schemas.clinical_intel import (
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

THERAPY_DB: dict[str, dict] = {
    **THERAPIES_GI,
    **THERAPIES_LIVER,
    **THERAPIES_HEME_RARE,
    **THERAPIES_DERM_RHEUM,
    "short bowel syndrome": {
        "normalized_term": "Short Bowel Syndrome",
        "aliases": [
            "SBS",
            "sbs",
            "short gut",
            "short bowel",
            "short bowel syndrome",
            "intestinal failure",
            "intestinal failure due to short bowel syndrome",
        ],
        "overview": (
            "Short bowel syndrome is a malabsorptive condition caused by substantial loss of functional small intestine, "
            "most often after surgical resection or due to congenital or acquired intestinal disease. "
            "It can lead to chronic diarrhea, dehydration, electrolyte abnormalities, weight loss, and dependence on parenteral nutrition in more severe cases."
        ),
        "symptoms": [
            "Chronic diarrhea or high stool output",
            "Weight loss and malnutrition",
            "Dehydration",
            "Fatigue and weakness",
            "Electrolyte disturbances",
        ],
        "diagnosis": [
            "Clinical history of major small bowel resection or intestinal dysfunction",
            "Assessment of nutritional status, hydration, and weight trends",
            "Laboratory evaluation for electrolyte abnormalities, micronutrient deficiencies, and liver function",
            "Clinical evaluation for dependence on parenteral nutrition or need for specialized nutritional support",
        ],
        "icd_codes": [
            ICDCode(
                code="K91.2",
                description="Postsurgical malabsorption, not elsewhere classified",
            ),
        ],
        "procedures": [
            Procedure(
                name="Parenteral nutrition administration",
                code=None,
                indication="Supportive management in patients with intestinal failure or severe malabsorption",
            ),
            Procedure(
                name="Small bowel resection",
                code=None,
                indication="Relevant surgical history and underlying cause in many patients with short bowel syndrome",
            ),
        ],
        "treatments": [
            Treatment(
                name="Parenteral nutrition",
                type="Supportive / nutritional",
                line="Severe disease / intestinal failure",
                notes="Used in patients unable to maintain hydration or nutrition enterally.",
            ),
            Treatment(
                name="Enteral nutrition optimization",
                type="Supportive / nutritional",
                line="Foundational management",
                notes="Dietary and fluid strategies are central to long-term care.",
            ),
            Treatment(
                name="Antidiarrheal therapy",
                type="Pharmacological",
                line="Symptom control",
                notes="Used to reduce stool output and improve fluid balance in selected patients.",
            ),
            Treatment(
                name="Teduglutide",
                type="Pharmacological / biologic",
                line="Selected patients with parenteral support dependence",
                notes="Used in appropriate patients to enhance intestinal absorption and reduce parenteral support needs.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Short bowel syndrome is often difficult to identify precisely in claims data without longitudinal clinical context.",
            "Parenteral nutrition use may act as an important proxy for disease severity or intestinal failure.",
            "Underlying etiology, bowel anatomy, and remnant bowel length are usually not fully captured in administrative datasets.",
        ],
    },
    "multiple myeloma": {
        "normalized_term": "Multiple Myeloma",
        "aliases": [
            "multiple myeloma",
            "mm",
            "myeloma",
            "plasma cell myeloma",
            "plasma cell malignancy",
        ],
        "overview": (
            "Multiple myeloma is a hematologic malignancy characterized by clonal proliferation of plasma cells in the bone marrow. "
            "It may cause anemia, bone disease, renal dysfunction, hypercalcemia, recurrent infections, and detectable monoclonal protein in serum or urine."
        ),
        "symptoms": [
            "Bone pain, especially back or rib pain",
            "Fatigue related to anemia",
            "Recurrent infections",
            "Renal dysfunction",
            "Hypercalcemia-related symptoms such as constipation, confusion, or weakness",
        ],
        "diagnosis": [
            "Serum and urine protein studies including SPEP, UPEP, immunofixation, and free light chain testing",
            "Bone marrow biopsy showing clonal plasma cell involvement",
            "Imaging evaluation for lytic bone lesions or other myeloma-defining bone disease",
            "Assessment for end-organ damage such as anemia, renal impairment, hypercalcemia, or bone lesions",
        ],
        "icd_codes": [
            ICDCode(
                code="C90.00",
                description="Multiple myeloma not having achieved remission",
            ),
            ICDCode(code="C90.01", description="Multiple myeloma in remission"),
            ICDCode(code="C90.02", description="Multiple myeloma in relapse"),
        ],
        "procedures": [
            Procedure(
                name="Bone marrow biopsy",
                code=None,
                indication="Diagnostic confirmation and disease characterization",
            ),
            Procedure(
                name="Serum protein electrophoresis",
                code=None,
                indication="Detection and monitoring of monoclonal protein",
            ),
            Procedure(
                name="Skeletal imaging",
                code=None,
                indication="Assessment of bone lesions and disease burden",
            ),
        ],
        "treatments": [
            Treatment(
                name="Proteasome inhibitor-based therapy",
                type="Pharmacological",
                line="Initial or relapsed therapy",
                notes="Often used as part of combination regimens.",
            ),
            Treatment(
                name="Immunomodulatory agents",
                type="Pharmacological",
                line="Initial or relapsed therapy",
                notes="Commonly used in combination treatment strategies.",
            ),
            Treatment(
                name="Anti-CD38 monoclonal antibodies",
                type="Pharmacological / biologic",
                line="Selected patients",
                notes="Used in frontline or relapsed settings depending on regimen and patient factors.",
            ),
            Treatment(
                name="Autologous stem cell transplant",
                type="Procedural / cellular therapy",
                line="Eligible patients",
                notes="Considered in transplant-eligible patients as part of treatment strategy.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="ICD-10-CM C90.0 Multiple myeloma",
                url="https://www.icd10data.com/ICD10CM/Codes/C00-D49/C81-C96/C90-/C90.0",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Line of therapy is difficult to infer from claims alone and often requires regimen construction logic.",
            "Oral and infused therapies may require integration of pharmacy and medical claims.",
            "Disease status such as remission, relapse, cytogenetic risk, and response depth may be incomplete in administrative data.",
        ],
    },
    "amyotrophic lateral sclerosis": {
        "normalized_term": "Amyotrophic Lateral Sclerosis",
        "aliases": [
            "amyotrophic lateral sclerosis",
            "als",
            "lou gehrig disease",
            "lou gehrig's disease",
            "motor neuron disease",
        ],
        "overview": (
            "Amyotrophic lateral sclerosis is a progressive neurodegenerative disorder affecting motor neurons, leading to worsening muscle weakness, loss of voluntary movement, speech and swallowing difficulties, and respiratory impairment over time."
        ),
        "symptoms": [
            "Progressive muscle weakness",
            "Muscle twitching or cramps",
            "Difficulty speaking or swallowing",
            "Gait difficulty or falls",
            "Respiratory weakness in advanced disease",
        ],
        "diagnosis": [
            "Neurologic examination showing progressive upper and lower motor neuron involvement",
            "Electromyography and nerve conduction studies to support diagnosis and exclude mimics",
            "Imaging and laboratory evaluation to rule out alternative causes",
            "Longitudinal clinical assessment of progressive motor decline",
        ],
        "icd_codes": [
            ICDCode(code="G12.21", description="Amyotrophic lateral sclerosis"),
        ],
        "procedures": [
            Procedure(
                name="Electromyography",
                code=None,
                indication="Support diagnosis and evaluate motor neuron involvement",
            ),
            Procedure(
                name="Pulmonary function testing",
                code=None,
                indication="Assessment of respiratory function and disease progression",
            ),
            Procedure(
                name="Feeding tube placement",
                code=None,
                indication="Nutritional support in selected patients with swallowing impairment",
            ),
        ],
        "treatments": [
            Treatment(
                name="Riluzole",
                type="Pharmacological",
                line="Disease-modifying / supportive",
                notes="Used to modestly slow disease progression in selected patients.",
            ),
            Treatment(
                name="Edaravone",
                type="Pharmacological",
                line="Selected patients",
                notes="Used in selected patients depending on clinical criteria and treatment access.",
            ),
            Treatment(
                name="Noninvasive ventilation",
                type="Supportive / respiratory",
                line="Respiratory support",
                notes="Used for respiratory muscle weakness and symptom support.",
            ),
            Treatment(
                name="Multidisciplinary supportive care",
                type="Supportive",
                line="Core management",
                notes="Includes speech, nutrition, respiratory, mobility, and palliative support.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIH NINDS Amyotrophic Lateral Sclerosis",
                url="https://www.ninds.nih.gov/health-information/disorders/amyotrophic-lateral-sclerosis-als",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "ALS progression severity is difficult to capture in claims without clinical measures such as functional rating scales.",
            "Durable medical equipment, respiratory support, feeding tube procedures, and specialty neurology visits may help characterize disease burden.",
            "Diagnosis timing may lag symptom onset, creating challenges for index-date definition.",
        ],
    },
}

ALIAS_INDEX: dict[str, str] = {}

for canonical, data in THERAPY_DB.items():
    ALIAS_INDEX[canonical.lower()] = canonical
    for alias in data.get("aliases", []):
        ALIAS_INDEX[alias.lower()] = canonical


def resolve_therapy_key(query: str) -> str | None:
    q = query.strip().lower()

    # 1. Exact match
    if q in ALIAS_INDEX:
        return ALIAS_INDEX[q]

    # 2. Partial match on aliases
    for alias, canonical in ALIAS_INDEX.items():
        if q in alias or alias in q:
            return canonical

    # 3. Partial match on canonical keys
    for key in THERAPY_DB:
        if q in key or key in q:
            return key

    return None


def suggest_therapies(query: str, limit: int = 3) -> list[str]:
    q = query.strip().lower()

    candidate_to_key: dict[str, str] = {}

    for key, data in THERAPY_DB.items():
        candidate_to_key[key.lower()] = key

        for alias in data.get("aliases", []):
            candidate_to_key[alias.lower()] = key

    matches = difflib.get_close_matches(
        q,
        list(candidate_to_key.keys()),
        n=limit,
        cutoff=0.15,
    )

    suggestions = []
    for match in matches:
        canonical_key = candidate_to_key[match]
        if canonical_key not in suggestions:
            suggestions.append(canonical_key)

    return suggestions
