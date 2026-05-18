from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_DERM_RHEUM = {
    "psoriasis": {
        "normalized_term": "Psoriasis",
        "aliases": [
            "psoriasis",
            "pso",
            "plaque psoriasis",
            "psoriasis vulgaris",
        ],
        "overview": (
            "Psoriasis is a chronic immune-mediated skin disease characterized by inflammatory, scaly plaques that may vary in extent and severity. "
            "It can be associated with systemic inflammation, comorbidities, and psoriatic arthritis in some patients.\n\n"
            "Global / U.S. Epidemiology: Psoriasis is common worldwide, with prevalence varying by geography and population. U.S. adult prevalence is commonly estimated around 3%."
        ),
        "causes": [
            "Chronic immune-mediated inflammation involving abnormal activation of skin and systemic inflammatory pathways.",
            "Disease activity is driven by genetic susceptibility, immune dysregulation, and environmental triggers.",
        ],
        "risk_factors": [
            "Family history of psoriasis",
            "Obesity",
            "Smoking",
            "Certain infections or skin trauma",
            "Stress and selected medication triggers",
        ],
        "symptoms": [
            "Red or inflamed scaly skin plaques",
            "Itching, burning, or soreness of affected skin",
            "Dry or cracked skin that may bleed",
            "Nail pitting or nail changes",
            "Joint pain or stiffness in patients with psoriatic arthritis",
        ],
        "diagnosis": [
            "Clinical skin examination by a clinician or dermatologist",
            "Assessment of lesion morphology, distribution, and severity",
            "Evaluation for nail disease and joint symptoms",
            "Skin biopsy in selected cases when diagnosis is uncertain",
        ],
        "diagnostic_considerations": [
            "Diagnosis is usually clinical based on plaque morphology, distribution, and chronicity.",
            "Assessment should consider severity, body surface area, sensitive locations, nail involvement, and psoriatic arthritis symptoms.",
            "Skin biopsy may be used when diagnosis is uncertain or mimics are suspected.",
            "Differential diagnosis may include eczema, seborrheic dermatitis, tinea, lichen planus, and cutaneous lupus.",
            "In real-world data, PASI score, body surface area, lesion location, and symptom burden are often not available.",
        ],
        "icd_codes": [
            ICDCode(code="L40.0", description="Psoriasis vulgaris"),
            ICDCode(code="L40.9", description="Psoriasis, unspecified"),
        ],
        "procedures": [
            Procedure(
                name="Skin examination",
                code=None,
                indication="Clinical diagnosis and severity assessment",
            ),
            Procedure(
                name="Skin biopsy",
                code=None,
                indication="Used selectively when diagnosis is uncertain",
            ),
            Procedure(
                name="Phototherapy",
                code=None,
                indication="Treatment option for selected patients with more extensive disease",
            ),
        ],
        "treatments": [
            Treatment(
                name="Topical corticosteroids",
                type="Pharmacological / topical",
                line="Mild to moderate disease",
                notes="Commonly used for localized plaques.",
            ),
            Treatment(
                name="Phototherapy",
                type="Procedural",
                line="Selected patients",
                notes="Used for more extensive or refractory skin disease.",
            ),
            Treatment(
                name="Conventional systemic therapy",
                type="Pharmacological",
                line="Moderate to severe disease",
                notes="Includes selected systemic immunomodulatory agents.",
            ),
            Treatment(
                name="Biologic or targeted therapy",
                type="Pharmacological / biologic",
                line="Moderate to severe disease",
                notes="Used in selected patients based on severity, comorbidities, and prior therapy.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIH NIAMS Psoriasis Diagnosis and Treatment",
                url="https://www.niams.nih.gov/health-topics/psoriasis/diagnosis-treatment-and-steps-to-take",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Claims data often lacks body surface area, PASI score, lesion location, and physician global assessment.",
            "Topical therapies may be undercaptured if paid out of pocket or inconsistently recorded.",
            "Differentiating psoriasis alone from psoriasis with psoriatic arthritis requires joint diagnosis, rheumatology care, or treatment pattern logic.",
        ],
    },
    "psoriatic arthritis": {
        "normalized_term": "Psoriatic Arthritis",
        "aliases": [
            "psoriatic arthritis",
            "psa",
            "ps arthritis",
            "arthritis with psoriasis",
        ],
        "overview": (
            "Psoriatic arthritis is a chronic inflammatory arthritis associated with psoriasis. "
            "It can involve peripheral joints, axial skeleton, entheses, digits, skin, and nails, and may lead to pain, stiffness, swelling, and structural damage if uncontrolled.\n\n"
            "Global / U.S. Epidemiology: Psoriatic arthritis occurs in a subset of patients with psoriasis. Estimates vary, but approximately 20% to 30% of patients with psoriasis may develop psoriatic arthritis."
        ),
        "causes": [
            "Chronic immune-mediated inflammation affecting joints, entheses, skin, nails, and sometimes the axial skeleton.",
            "Disease development is associated with genetic susceptibility, psoriasis-related inflammation, and environmental triggers.",
        ],
        "risk_factors": [
            "Personal history of psoriasis",
            "Family history of psoriasis or psoriatic arthritis",
            "Nail psoriasis",
            "Obesity",
            "History of severe or extensive skin disease",
        ],
        "symptoms": [
            "Joint pain, swelling, or stiffness",
            "Morning stiffness",
            "Dactylitis or swelling of an entire finger or toe",
            "Enthesitis such as heel or tendon insertion pain",
            "Psoriasis skin lesions or nail changes",
        ],
        "diagnosis": [
            "Clinical evaluation of joint symptoms, skin findings, and nail changes",
            "Assessment for inflammatory arthritis patterns including peripheral, axial, enthesitis, or dactylitis involvement",
            "Laboratory testing to help exclude rheumatoid arthritis or other mimics",
            "Imaging to assess joint damage, enthesitis, or axial involvement when clinically appropriate",
        ],
        "diagnostic_considerations": [
            "Diagnosis is clinical and requires assessment of inflammatory joint, enthesis, axial, skin, and nail involvement.",
            "Psoriatic arthritis should be distinguished from rheumatoid arthritis, osteoarthritis, gout, axial spondyloarthritis, and mechanical joint disease.",
            "CASPAR criteria may support classification in research settings.",
            "Disease domains such as dactylitis, enthesitis, axial disease, peripheral arthritis, skin disease, and nail disease influence treatment selection.",
            "In real-world data, disease domains and severity are often poorly captured without rheumatology notes, imaging, or structured clinical assessments.",
        ],
        "icd_codes": [
            ICDCode(code="L40.50", description="Arthropathic psoriasis, unspecified"),
            ICDCode(code="L40.59", description="Other psoriatic arthropathy"),
        ],
        "procedures": [
            Procedure(
                name="Rheumatologic examination",
                code=None,
                indication="Assessment of inflammatory joint and enthesis involvement",
            ),
            Procedure(
                name="Joint imaging",
                code=None,
                indication="Evaluation of structural damage or inflammatory involvement",
            ),
            Procedure(
                name="Inflammatory marker testing",
                code=None,
                indication="Supportive evaluation and exclusion of other inflammatory arthritides",
            ),
        ],
        "treatments": [
            Treatment(
                name="Nonsteroidal anti-inflammatory drugs",
                type="Pharmacological",
                line="Mild symptoms / symptom control",
                notes="Used for pain and inflammation control in selected patients.",
            ),
            Treatment(
                name="Conventional synthetic DMARDs",
                type="Pharmacological",
                line="Peripheral arthritis",
                notes="Used in selected patients with inflammatory peripheral joint disease.",
            ),
            Treatment(
                name="Biologic therapy",
                type="Pharmacological / biologic",
                line="Moderate to severe disease",
                notes="Used when disease activity, domains, or prior response support advanced therapy.",
            ),
            Treatment(
                name="Targeted synthetic therapy",
                type="Pharmacological",
                line="Selected patients",
                notes="Used in selected patients based on disease domains and treatment history.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIH NIAMS Psoriatic Arthritis Diagnosis and Treatment",
                url="https://www.niams.nih.gov/health-topics/psoriatic-arthritis/diagnosis-treatment-and-steps-to-take",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Disease domain involvement such as enthesitis, dactylitis, axial disease, and skin severity is often poorly captured in claims.",
            "Psoriatic arthritis may be confused with psoriasis alone unless joint diagnosis, rheumatology care, or treatment pattern criteria are applied.",
            "Advanced therapy exposure may require combining medical and pharmacy claims for injected, infused, and oral therapies.",
        ],
    },
    "colorectal cancer": {
        "normalized_term": "Colorectal Cancer",
        "aliases": [
            "colorectal cancer",
            "crc",
            "colon cancer",
            "rectal cancer",
            "colon carcinoma",
            "rectal carcinoma",
        ],
        "overview": (
            "Colorectal cancer is a malignancy arising in the colon or rectum. It may develop from precancerous polyps and can present with bowel habit changes, bleeding, anemia, abdominal symptoms, or be detected through screening before symptoms occur.\n\n"
            "Global / U.S. Epidemiology: Colorectal cancer is one of the most common cancers worldwide. In the United States, it remains a major cause of cancer incidence and mortality, with risk increasing with age."
        ),
        "causes": [
            "Malignant transformation of epithelial cells in the colon or rectum, often through adenoma-carcinoma sequence or serrated pathway mechanisms.",
            "Tumor development may involve accumulated genetic and epigenetic alterations, microsatellite instability, chromosomal instability, or inherited cancer syndromes.",
        ],
        "risk_factors": [
            "Older age",
            "Family history of colorectal cancer or advanced adenomas",
            "Inflammatory bowel disease involving the colon",
            "Lynch syndrome or familial adenomatous polyposis",
            "Obesity, smoking, heavy alcohol use, low physical activity, and diet-related factors",
        ],
        "symptoms": [
            "Change in bowel habits",
            "Blood in stool or rectal bleeding",
            "Abdominal pain or cramping",
            "Unexplained weight loss",
            "Iron deficiency anemia or fatigue",
        ],
        "diagnosis": [
            "Colonoscopy with biopsy for diagnostic confirmation",
            "Pathology review to confirm histology and tumor features",
            "Imaging for staging and evaluation of metastatic disease",
            "Molecular testing when clinically appropriate for treatment planning",
        ],
        "diagnostic_considerations": [
            "Diagnosis requires tissue confirmation, usually through colonoscopy with biopsy.",
            "Tumor location, stage, histology, molecular markers, and metastatic status are central to treatment planning.",
            "Screening history and detection pathway may influence stage at diagnosis.",
            "Molecular testing may include mismatch repair or microsatellite instability status and other biomarkers depending on disease setting.",
            "In real-world data, stage, recurrence, biomarkers, pathology details, and intent of therapy are often incompletely captured.",
        ],
        "icd_codes": [
            ICDCode(
                code="C18.9", description="Malignant neoplasm of colon, unspecified"
            ),
            ICDCode(
                code="C19", description="Malignant neoplasm of rectosigmoid junction"
            ),
            ICDCode(code="C20", description="Malignant neoplasm of rectum"),
        ],
        "procedures": [
            Procedure(
                name="Colonoscopy with biopsy",
                code="45380",
                indication="Diagnostic confirmation and tissue sampling",
            ),
            Procedure(
                name="Surgical resection",
                code=None,
                indication="Definitive management in selected localized disease",
            ),
            Procedure(
                name="CT imaging",
                code=None,
                indication="Staging and evaluation of metastatic disease",
            ),
        ],
        "treatments": [
            Treatment(
                name="Surgical resection",
                type="Procedural / surgical",
                line="Localized disease",
                notes="Used for selected colon or rectal cancers depending on stage and location.",
            ),
            Treatment(
                name="Chemotherapy",
                type="Pharmacological",
                line="Adjuvant or advanced disease",
                notes="Used depending on stage, recurrence risk, and metastatic setting.",
            ),
            Treatment(
                name="Radiation therapy",
                type="Radiation / local therapy",
                line="Selected rectal cancer",
                notes="Often relevant in rectal cancer management depending on stage and treatment plan.",
            ),
            Treatment(
                name="Targeted or immunotherapy",
                type="Pharmacological / biologic",
                line="Selected advanced disease",
                notes="Used based on biomarkers and disease characteristics.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="CDC Colorectal Cancer Screening",
                url="https://www.cdc.gov/colorectal-cancer/screening/index.html",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Colon and rectal cancer may need separate cohort logic depending on study objective.",
            "Stage, biomarkers, and recurrence status are often incomplete in claims data.",
            "Screening, diagnostic colonoscopy, surgery, systemic therapy, and radiation may need to be integrated longitudinally.",
        ],
    },
}
