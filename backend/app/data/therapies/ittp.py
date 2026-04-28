from app.schemas.clinical_intel import (
    ClinicalTrial,
    ICDCode,
    LiteratureReference,
    Procedure,
    Source,
    Treatment,
)

ITTP = {
    "normalized_term": "Immune Thrombotic Thrombocytopenic Purpura",
    "aliases": [
        "iTTP",
        "immune TTP",
        "thrombotic thrombocytopenic purpura",
    ],
    "overview": (
        "Immune thrombotic thrombocytopenic purpura is a rare, life-threatening thrombotic "
        "microangiopathy caused by severe ADAMTS13 deficiency, usually due to acquired "
        "autoantibodies. It is characterized by thrombocytopenia, microangiopathic hemolytic "
        "anemia, and risk of neurologic, cardiac, renal, and other organ ischemia, requiring "
        "urgent recognition and treatment."
    ),
    "symptoms": [
        "Fatigue and weakness",
        "Petechiae or bruising",
        "Neurologic symptoms such as confusion or headache",
        "Abdominal pain or nausea",
        "Shortness of breath",
    ],
    "diagnosis": [
        "CBC showing thrombocytopenia and anemia",
        "Evidence of hemolysis such as elevated LDH and schistocytes",
        "Severely reduced ADAMTS13 activity, often below 10%",
        "Clinical evaluation for thrombotic microangiopathy and urgent treatment need before confirmatory results if suspicion is high",
    ],
    "icd_codes": [
        ICDCode(code="M31.1", description="Thrombotic microangiopathy"),
    ],
    "procedures": [
        Procedure(
            name="ADAMTS13 activity test",
            code="85397",
            indication="Support diagnostic confirmation and disease characterization",
        ),
        Procedure(
            name="Therapeutic plasma exchange",
            code="36514",
            indication="Core acute management procedure",
        ),
    ],
    "treatments": [
        Treatment(
            name="Therapeutic plasma exchange",
            type="Supportive / procedural",
            line="Acute management",
            notes="A central therapy in acute episodes.",
        ),
        Treatment(
            name="Corticosteroids",
            type="Pharmacological",
            line="Acute management",
            notes="Often used with plasma exchange.",
        ),
        Treatment(
            name="Caplacizumab",
            type="Pharmacological",
            line="Adjunct",
            notes="Used in appropriate acute settings.",
        ),
        Treatment(
            name="Rituximab",
            type="Pharmacological",
            line="Adjunct / relapse prevention",
            notes="Often considered in refractory or relapsing disease.",
        ),
    ],
    "clinical_trials": [
        ClinicalTrial(
            nct_id="NCT03237767",
            title="Caplacizumab in acquired thrombotic thrombocytopenic purpura",
            phase="Phase 3",
            status="Completed",
            sponsor="Ablynx",
            url="https://clinicaltrials.gov/study/NCT03237767",
        ),
    ],
    "literature": [
        LiteratureReference(
            title="International Society on Thrombosis and Haemostasis guidelines for thrombotic thrombocytopenic purpura",
            authors="Zheng XL et al.",
            journal="Journal of Thrombosis and Haemostasis",
            year=2020,
            doi="10.1111/jth.15006",
            evidence_level="High",
        ),
    ],
    "sources": [
        Source(
            name="ClinicalTrials.gov",
            url="https://clinicaltrials.gov",
            accessed="2026-03-29",
        ),
    ],
    "data_considerations": [
        "Claims and EMR sources may capture different parts of the iTTP care journey.",
        "ADAMTS13 testing may be sparse or delayed in some real-world datasets.",
        "Procedure and diagnosis signals may not appear on the same claims row and often need staged logic.",
    ],
}