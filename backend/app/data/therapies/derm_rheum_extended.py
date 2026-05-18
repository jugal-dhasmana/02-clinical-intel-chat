from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_DERM_RHEUM_EXT = {
    "rheumatoid arthritis": {
        "normalized_term": "Rheumatoid Arthritis",
        "aliases": ["ra", "rheumatoid arthritis", "inflammatory arthritis ra"],
        "overview": (
            "Rheumatoid arthritis is a chronic autoimmune inflammatory disease characterized by symmetric inflammatory polyarthritis that can lead to joint damage, disability, and systemic complications.\n\n"
            "Global / U.S. Epidemiology: Rheumatoid arthritis affects populations worldwide, with global prevalence commonly estimated around 0.5% to 1.0%. Prevalence varies by age, sex, geography, and case definition."
        ),
        "causes": [
            "Autoimmune inflammation targeting synovial joints and related tissues.",
            "Disease development is multifactorial, involving genetic susceptibility, immune dysregulation, and environmental exposures.",
        ],
        "risk_factors": [
            "Female sex",
            "Older age",
            "Smoking",
            "Obesity",
            "Family history of rheumatoid arthritis or autoimmune disease",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is based on inflammatory joint symptoms, clinical examination, serology, inflammatory markers, and imaging when appropriate.",
            "Rheumatoid factor and anti-CCP antibodies support diagnosis but are not required in all patients.",
            "Differential diagnosis may include osteoarthritis, psoriatic arthritis, lupus, viral arthritis, gout, and other inflammatory arthritides.",
            "Early diagnosis and treatment are important to reduce risk of joint damage and disability.",
            "In real-world data, disease activity scores, serology, imaging findings, and functional status are often incompletely captured.",
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
        "overview": (
            "Atopic dermatitis is a chronic inflammatory skin condition characterized by pruritus, eczematous lesions, and relapsing disease course.\n\n"
            "Global / U.S. Epidemiology: Atopic dermatitis is common worldwide and is more frequent in children than adults. Recent estimates in Europe and the United States suggest prevalence around 20% among children and roughly 7% to 14% among adults."
        ),
        "causes": [
            "Chronic inflammatory skin disease involving skin barrier dysfunction and immune dysregulation.",
            "Disease activity may be influenced by genetic susceptibility, environmental exposures, allergens, irritants, and microbiome changes.",
        ],
        "risk_factors": [
            "Personal or family history of atopic disease",
            "Asthma or allergic rhinitis",
            "Filaggrin or skin barrier-related genetic susceptibility",
            "Early childhood onset",
            "Environmental triggers such as irritants, allergens, climate, or infections",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is usually clinical based on chronic or relapsing eczematous lesions and pruritus.",
            "Severity assessment may include body surface area, lesion distribution, itch intensity, sleep disturbance, and quality-of-life impact.",
            "Differential diagnosis may include contact dermatitis, psoriasis, seborrheic dermatitis, scabies, cutaneous T-cell lymphoma, and immunodeficiency-related dermatitis.",
            "Atopic comorbidities such as asthma, allergic rhinitis, and food allergy may be relevant in selected patients.",
            "In real-world data, itch severity, lesion extent, sleep impairment, and patient-reported burden are often poorly captured.",
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
        "overview": (
            "Systemic lupus erythematosus is a chronic autoimmune disease affecting multiple organ systems, often with periods of flares and remission. "
            "Clinical involvement may include skin, joints, kidneys, blood, nervous system, and other organs.\n\n"
            "Global / U.S. Epidemiology: SLE prevalence varies widely by ancestry, sex, geography, and case definition. It is more common among women and disproportionately affects Black, Hispanic, Asian, and Indigenous populations."
        ),
        "causes": [
            "Autoimmune disease involving loss of immune tolerance and production of autoantibodies.",
            "Disease development is multifactorial, involving genetic susceptibility, hormonal influences, immune dysregulation, and environmental triggers.",
        ],
        "risk_factors": [
            "Female sex",
            "Family history of lupus or autoimmune disease",
            "Black, Hispanic, Asian, or Indigenous ancestry",
            "Younger to middle adult age",
            "Environmental triggers such as ultraviolet light, infections, or selected medications",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis requires integration of clinical features, autoantibody testing, complement levels, and organ-specific evaluation.",
            "ANA testing is sensitive but not specific, so interpretation requires clinical context.",
            "Organ involvement, especially lupus nephritis, strongly affects disease severity and management.",
            "Differential diagnosis may include rheumatoid arthritis, Sjögren’s disease, antiphospholipid syndrome, infection, malignancy, and drug-induced lupus.",
            "In real-world data, disease activity, flare severity, organ involvement, autoantibody profiles, and complement levels may be incompletely captured.",
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
        "overview": (
            "Ankylosing spondylitis is a chronic inflammatory disease primarily affecting the spine and sacroiliac joints. "
            "It can cause inflammatory back pain, stiffness, reduced spinal mobility, peripheral arthritis, enthesitis, and extra-articular manifestations.\n\n"
            "Global / U.S. Epidemiology: Ankylosing spondylitis prevalence varies by geography and HLA-B27 distribution. U.S. axial spondyloarthritis prevalence estimates have been reported around 0.9% to 1.4% among adults, with narrower estimates for ankylosing spondylitis specifically."
        ),
        "causes": [
            "Chronic immune-mediated inflammation involving the sacroiliac joints, spine, entheses, and sometimes peripheral joints.",
            "Disease development is strongly associated with genetic susceptibility, particularly HLA-B27, though not all carriers develop disease.",
        ],
        "risk_factors": [
            "HLA-B27 positivity",
            "Family history of ankylosing spondylitis or spondyloarthritis",
            "Male sex",
            "Younger adult age at symptom onset",
            "Personal history of inflammatory bowel disease, psoriasis, or uveitis",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is based on inflammatory back pain features, physical examination, imaging, and clinical context.",
            "MRI may detect active sacroiliitis before structural changes are visible on X-ray.",
            "HLA-B27 supports diagnosis but is not diagnostic by itself.",
            "Differential diagnosis may include mechanical back pain, degenerative spine disease, fibromyalgia, infection, and other spondyloarthritis conditions.",
            "In real-world data, symptom onset timing, imaging findings, HLA-B27 status, and disease activity are often incompletely captured.",
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
        "overview": (
            "Hidradenitis suppurativa is a chronic inflammatory skin disease characterized by painful nodules, abscesses, tunnels, drainage, and scarring, commonly affecting intertriginous areas.\n\n"
            "Global / U.S. Epidemiology: Hidradenitis suppurativa prevalence varies widely by study design and case definition. U.S. estimates are often reported around 0.1% to 1%, with underdiagnosis likely."
        ),
        "causes": [
            "Chronic inflammatory disease involving follicular occlusion, immune dysregulation, and recurrent inflammation of hair follicle-bearing skin.",
            "Disease mechanisms may involve genetic susceptibility, hormonal factors, microbiome changes, and inflammatory pathway activation.",
        ],
        "risk_factors": [
            "Female sex",
            "Family history of hidradenitis suppurativa",
            "Obesity",
            "Smoking",
            "Metabolic syndrome or other inflammatory comorbidities",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is clinical and based on typical lesions, characteristic locations, and chronic or recurrent course.",
            "Commonly affected sites include axillae, groin, perineal, inframammary, and other intertriginous areas.",
            "Severity may be assessed using Hurley stage or lesion burden, but these are often absent from routine data.",
            "Differential diagnosis may include recurrent abscesses, folliculitis, furunculosis, Crohn’s-related perianal disease, and infected cysts.",
            "In real-world data, disease severity, lesion location, drainage, tunnels, scarring, and quality-of-life burden are often poorly captured.",
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
