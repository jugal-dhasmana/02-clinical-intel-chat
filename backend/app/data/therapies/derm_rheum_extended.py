from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_DERM_RHEUM_EXT = {
    "rheumatoid arthritis": {
        "normalized_term": "Rheumatoid Arthritis",
        "aliases": ["ra", "rheumatoid arthritis", "inflammatory arthritis ra"],
        "overview": "Rheumatoid arthritis is a chronic autoimmune disease characterized by symmetric inflammatory polyarthritis leading to joint damage, disability, and systemic complications.",
        "symptoms": [
            "Joint pain and swelling",
            "Morning stiffness lasting more than 30 minutes",
            "Fatigue",
            "Reduced joint function",
            "Systemic symptoms in severe disease",
        ],
        "diagnosis": [
            "Clinical evaluation of joint involvement and symmetry",
            "Serologic testing including rheumatoid factor and anti-CCP",
            "Imaging such as X-ray or ultrasound",
            "Assessment of inflammatory markers",
        ],
        "icd_codes": [
            ICDCode(code="M06.9", description="Rheumatoid arthritis, unspecified")
        ],
        "procedures": [
            Procedure(
                name="Joint imaging", code=None, indication="Assess structural damage"
            ),
            Procedure(
                name="Serologic testing",
                code=None,
                indication="Confirm autoimmune markers",
            ),
        ],
        "treatments": [
            Treatment(
                name="DMARDs",
                type="Pharmacological",
                line="First-line",
                notes="Methotrexate commonly used",
            ),
            Treatment(
                name="Biologic therapy",
                type="Pharmacological",
                line="Moderate to severe",
                notes="TNF inhibitors and others",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Disease severity often requires lab and imaging data beyond claims",
            "Treatment pathways vary significantly by severity and response",
        ],
    },
    "atopic dermatitis": {
        "normalized_term": "Atopic Dermatitis",
        "aliases": ["eczema", "atopic dermatitis", "ad eczema"],
        "overview": "Atopic dermatitis is a chronic inflammatory skin condition characterized by pruritus, eczema, and relapsing disease course.",
        "symptoms": [
            "Itchy skin",
            "Red inflamed patches",
            "Dry or cracked skin",
            "Sleep disturbance",
            "Skin infections in severe cases",
        ],
        "diagnosis": [
            "Clinical evaluation of skin lesions",
            "History of atopy or allergic disease",
            "Assessment of chronic or relapsing course",
        ],
        "icd_codes": [
            ICDCode(code="L20.9", description="Atopic dermatitis, unspecified")
        ],
        "procedures": [
            Procedure(
                name="Skin examination",
                code=None,
                indication="Diagnosis and severity assessment",
            )
        ],
        "treatments": [
            Treatment(
                name="Topical corticosteroids",
                type="Pharmacological",
                line="First-line",
            ),
            Treatment(
                name="Biologic therapy",
                type="Pharmacological",
                line="Moderate to severe",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Severity assessment often missing in claims",
            "Treatment escalation indicates disease burden",
        ],
    },
    "systemic lupus erythematosus": {
        "normalized_term": "Systemic Lupus Erythematosus",
        "aliases": ["sle", "lupus"],
        "overview": "Systemic lupus erythematosus is a chronic autoimmune disease affecting multiple organ systems with periods of flares and remission.",
        "symptoms": [
            "Fatigue",
            "Joint pain",
            "Skin rash",
            "Renal involvement",
            "Systemic inflammation",
        ],
        "diagnosis": [
            "Clinical criteria with multi-organ involvement",
            "Autoantibody testing including ANA",
            "Laboratory evaluation of organ involvement",
        ],
        "icd_codes": [
            ICDCode(code="M32.9", description="Systemic lupus erythematosus")
        ],
        "procedures": [],
        "treatments": [
            Treatment(
                name="Immunosuppressants",
                type="Pharmacological",
                line="Moderate to severe",
            ),
            Treatment(
                name="Biologic therapy",
                type="Pharmacological",
                line="Selected patients",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Multi-organ disease requires integrated datasets",
            "Claims alone may undercapture severity",
        ],
    },
    "ankylosing spondylitis": {
        "normalized_term": "Ankylosing Spondylitis",
        "aliases": ["as disease", "ankylosing spondylitis"],
        "overview": "Ankylosing spondylitis is a chronic inflammatory disease primarily affecting the spine and sacroiliac joints.",
        "symptoms": [
            "Chronic back pain",
            "Morning stiffness",
            "Reduced spinal mobility",
            "Fatigue",
            "Peripheral joint involvement",
        ],
        "diagnosis": [
            "Clinical evaluation of inflammatory back pain",
            "Imaging such as MRI of sacroiliac joints",
            "HLA-B27 testing in selected patients",
        ],
        "icd_codes": [ICDCode(code="M45.9", description="Ankylosing spondylitis")],
        "procedures": [],
        "treatments": [
            Treatment(name="NSAIDs", type="Pharmacological", line="First-line"),
            Treatment(
                name="Biologic therapy",
                type="Pharmacological",
                line="Moderate to severe",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Imaging findings not available in claims",
            "Diagnosis may be delayed due to nonspecific symptoms",
        ],
    },
    "hidradenitis suppurativa": {
        "normalized_term": "Hidradenitis Suppurativa",
        "aliases": ["hs disease", "hidradenitis"],
        "overview": "Hidradenitis suppurativa is a chronic inflammatory skin condition characterized by painful nodules, abscesses, and sinus tract formation.",
        "symptoms": [
            "Painful skin nodules",
            "Recurrent abscesses",
            "Drainage from lesions",
            "Scarring",
            "Chronic inflammation",
        ],
        "diagnosis": [
            "Clinical evaluation of recurrent lesions",
            "Assessment of lesion distribution and chronicity",
            "History of chronic and relapsing disease course",
        ],
        "icd_codes": [ICDCode(code="L73.2", description="Hidradenitis suppurativa")],
        "procedures": [],
        "treatments": [
            Treatment(
                name="Antibiotics", type="Pharmacological", line="Mild to moderate"
            ),
            Treatment(
                name="Biologic therapy",
                type="Pharmacological",
                line="Moderate to severe",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Disease severity often underreported",
            "Repeated encounters may indicate severity",
        ],
    },
}
