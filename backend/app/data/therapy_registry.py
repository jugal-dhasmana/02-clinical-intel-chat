import difflib
from app.data.therapies.gi import THERAPIES_GI
from app.data.therapies.liver import THERAPIES_LIVER
from app.data.therapies.heme_rare import THERAPIES_HEME_RARE
from app.data.therapies.derm_rheum import THERAPIES_DERM_RHEUM
from app.data.therapies.derm_rheum_extended import THERAPIES_DERM_RHEUM_EXT
from app.data.therapies.gi_extended import THERAPIES_GI_ONCOLOGY
from app.data.therapies.cardiology import THERAPIES_CARDIOLOGY
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
    **THERAPIES_DERM_RHEUM_EXT,
    **THERAPIES_GI_ONCOLOGY,
    **THERAPIES_CARDIOLOGY,    
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
            "Short bowel syndrome is a malabsorptive condition caused by substantial loss of functional small intestine, most often after surgical resection or due to congenital or acquired intestinal disease. "
            "It can lead to chronic diarrhea, dehydration, electrolyte abnormalities, weight loss, and dependence on parenteral nutrition in more severe cases.\n\n"
            "Global / U.S. Epidemiology: Short bowel syndrome is rare but clinically significant. "
            "Prevalence estimates vary by definition and severity, with intestinal failure requiring long-term parenteral nutrition representing the most severe end of the disease spectrum."
        ),
        "causes": [
            "Loss of functional small intestine resulting in reduced nutrient, fluid, and electrolyte absorption.",
            "Common underlying causes include bowel resection, Crohn’s disease, mesenteric ischemia, trauma, congenital abnormalities, or radiation-related injury.",
        ],
        "risk_factors": [
            "Major small bowel resection",
            "Crohn’s disease or inflammatory bowel disease complications",
            "Mesenteric ischemia",
            "Congenital intestinal disorders",
            "Radiation injury or abdominal surgical complications",
        ],
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
        "diagnostic_considerations": [
            "Short bowel syndrome diagnosis depends on clinical history, intestinal anatomy, malabsorption severity, and functional nutritional status.",
            "Underlying cause, remaining bowel length, colon continuity, and presence of ileocecal valve may significantly influence disease severity and nutritional dependence.",
            "Patients may develop intestinal failure requiring long-term parenteral nutrition, fluid support, or specialized nutritional management.",
            "Complications such as dehydration, electrolyte abnormalities, micronutrient deficiencies, liver disease, and catheter-related infections may require longitudinal monitoring.",
            "In real-world data, bowel anatomy, residual bowel length, nutritional status, and intestinal adaptation are often poorly captured in administrative datasets.",
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
            "Amyotrophic lateral sclerosis is a progressive neurodegenerative disorder affecting upper and lower motor neurons, leading to worsening muscle weakness, loss of voluntary movement, speech and swallowing difficulties, and respiratory impairment over time.\n\n"
            "Global / U.S. Epidemiology: ALS is rare, with prevalence commonly estimated around 4 to 6 cases per 100,000 people. U.S. estimates suggest approximately 30,000 individuals are living with ALS."
        ),
        "causes": [
            "Progressive degeneration of upper and lower motor neurons.",
            "Most cases are sporadic, while a smaller proportion are familial and associated with genetic variants such as C9orf72, SOD1, TARDBP, or FUS.",
        ],
        "risk_factors": [
            "Older age",
            "Male sex",
            "Family history of ALS or motor neuron disease",
            "Genetic susceptibility in familial ALS",
            "Possible environmental or occupational exposures, although causal relationships are not always clear",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is based on progressive upper and lower motor neuron involvement with exclusion of mimicking conditions.",
            "Electromyography and nerve conduction studies support diagnosis and help assess lower motor neuron involvement.",
            "MRI and laboratory testing may be used to exclude structural, inflammatory, infectious, metabolic, or neuromuscular mimics.",
            "Respiratory and swallowing function should be assessed longitudinally because they strongly influence prognosis and care needs.",
            "In real-world data, functional decline, ALSFRS-R score, respiratory metrics, and symptom onset timing are often incompletely captured.",
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

    # 1. Exact match only against canonical keys and aliases
    if q in ALIAS_INDEX:
        return ALIAS_INDEX[q]

    # 2. No loose partial matching for clinical terms.
    # Unsupported terms should return Not Curated instead of guessing.
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
