import difflib
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
    # paste ALL your therapies here (ittp, multiple myeloma, hemophilia a, etc.)
    "ittp": {
        "normalized_term": "Immune Thrombotic Thrombocytopenic Purpura",
        "aliases": [
            "iTTP",
            "ittp",
            "i ttp",
            "immune ttp",
            "acquired ttp",
            "thrombotic thrombocytopenic purpura",
            "immune thrombotic thrombocytopenic purpura",
            "adamts13 deficiency",
        ],
        "overview": (
            "Immune thrombotic thrombocytopenic purpura is a rare, life-threatening thrombotic microangiopathy caused by severe ADAMTS13 deficiency, usually due to acquired autoantibodies. It is characterized by thrombocytopenia, microangiopathic hemolytic anemia, and risk of neurologic, cardiac, renal, and other organ ischemia, requiring urgent recognition and treatment."
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
            "Severely reduced ADAMTS13 activity, often <10%",
            "Clinical evaluation for TMA and urgent treatment need before confirmatory results if suspicion is high",
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
                phase=TrialPhase.PHASE_3,
                status=TrialStatus.COMPLETED,
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
                doi="https://doi.org/10.1111/jth.15006",
                evidence_level=EvidenceLevel.HIGH,
            )
        ],
        "sources": [
            Source(
                name="ClinicalTrials.gov",
                url="https://clinicaltrials.gov",
                accessed="2026-03-29",
            ),
        ],
        "data_considerations": [
            "Claims and EMR sources may capture different parts of the iTTP journey.",
            "ADAMTS13 testing may be sparse or delayed in some real-world datasets.",
            "Procedure and diagnosis signals may not appear on the same claims row and often need staged logic.",
        ],
    },
    "multiple myeloma": {
        "normalized_term": "Multiple Myeloma",
        "aliases": ["MM"],
        "overview": "Multiple myeloma is a plasma cell malignancy characterized by clonal proliferation in the bone marrow and end-organ damage in selected patients.",
        "symptoms": [
            "Bone pain",
            "Anemia-related fatigue",
            "Renal dysfunction",
            "Recurrent infections",
        ],
        "diagnosis": [
            "Serum and urine protein studies",
            "Bone marrow evaluation",
            "Imaging as clinically appropriate",
        ],
        "icd_codes": [ICDCode(code="C90.0", description="Multiple myeloma")],
        "procedures": [
            Procedure(name="Bone marrow biopsy", indication="Diagnostic evaluation")
        ],
        "treatments": [
            Treatment(name="Proteasome inhibitors", type="Pharmacological"),
            Treatment(name="Immunomodulatory agents", type="Pharmacological"),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Lines of therapy can be difficult to infer cleanly from claims alone."
        ],
    },
    "hemophilia a": {
        "normalized_term": "Hemophilia A",
        "aliases": [
            "factor viii deficiency",
            "hemophilia a",
            "haemophilia a",
            "hem a",
            "factor 8",
            "factor 8 deficiency",
            "factor viii",
            "fviii deficiency",
        ],
        "overview": (
            "Hemophilia A is an inherited X-linked bleeding disorder caused by deficiency of clotting factor VIII, "
            "leading to impaired blood coagulation. It is characterized by spontaneous bleeding episodes, particularly "
            "into joints and muscles, and severity depends on the level of factor VIII activity."
        ),
        "symptoms": [
            "Easy bruising",
            "Joint bleeding (hemarthrosis)",
            "Prolonged bleeding after injury or surgery",
            "Muscle hematomas",
            "Spontaneous bleeding in severe cases",
        ],
        "diagnosis": [
            "Factor VIII activity assay showing reduced levels",
            "Prolonged activated partial thromboplastin time (aPTT) with normal prothrombin time (PT)",
            "Bleeding history and family history consistent with inherited disorder",
        ],
        "icd_codes": [
            ICDCode(code="D66", description="Hereditary factor VIII deficiency"),
        ],
        "procedures": [
            Procedure(
                name="Factor VIII activity assay",
                code=None,
                indication="Confirm diagnosis and assess severity",
            ),
            Procedure(
                name="aPTT test", code=None, indication="Initial coagulation screening"
            ),
        ],
        "treatments": [
            Treatment(
                name="Factor VIII replacement therapy",
                type="Pharmacological / biologic",
                line="Standard therapy",
                notes="Used for both prophylaxis and treatment of bleeding episodes.",
            ),
            Treatment(
                name="Emicizumab",
                type="Pharmacological / biologic",
                line="Prophylaxis",
                notes="Used to reduce bleeding frequency in selected patients.",
            ),
            Treatment(
                name="Desmopressin (DDAVP)",
                type="Pharmacological",
                line="Mild disease",
                notes="Used in mild hemophilia A to temporarily increase factor VIII levels.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Severity classification based on factor VIII activity is often not available in claims data.",
            "Bleeding events may be underreported or inconsistently coded in administrative datasets.",
            "Treatment patterns require integration of pharmacy and medical claims to capture factor replacement and prophylaxis.",
        ],
    },
    "crohns disease": {
        "normalized_term": "Crohn's Disease",
        "aliases": [
            "crohn",
            "crohns",
            "crohn disease",
            "crohns disease",
            "crohn disease",
            "cd",
            "crohn's disease",
            "ibd crohn",
        ],
        "overview": (
            "Crohn's disease is a chronic inflammatory bowel disease characterized by transmural "
            "inflammation that can affect any part of the gastrointestinal tract, most commonly the "
            "terminal ileum and colon. It often follows a relapsing and remitting course and may lead "
            "to complications such as strictures, fistulas, abscesses, and nutritional deficiencies."
        ),
        "symptoms": [
            "Chronic diarrhea",
            "Abdominal pain and cramping",
            "Weight loss",
            "Fatigue",
            "Rectal bleeding in some patients",
        ],
        "diagnosis": [
            "Clinical history and physical examination",
            "Colonoscopy with ileoscopy and biopsy",
            "Cross-sectional imaging such as CT enterography or MR enterography",
            "Inflammatory markers and stool testing including fecal calprotectin",
        ],
        "icd_codes": [
            ICDCode(
                code="K50.90",
                description="Crohn's disease, unspecified, without complications",
            ),
        ],
        "procedures": [
            Procedure(
                name="Colonoscopy with biopsy",
                code="45380",
                indication="Diagnostic evaluation and tissue confirmation",
            ),
            Procedure(
                name="MR enterography",
                code=None,
                indication="Assessment of small bowel involvement and complications",
            ),
        ],
        "treatments": [
            Treatment(
                name="Corticosteroids",
                type="Pharmacological",
                line="Induction",
                notes="Used for short-term control of active inflammation, not for long-term maintenance.",
            ),
            Treatment(
                name="Anti-TNF therapy",
                type="Pharmacological / biologic",
                line="Moderate to severe disease",
                notes="Used in selected patients with moderate to severe or fistulizing disease.",
            ),
            Treatment(
                name="Immunomodulators",
                type="Pharmacological",
                line="Maintenance / steroid-sparing",
                notes="Used in selected patients for maintenance or combination strategies.",
            ),
            Treatment(
                name="Surgical intervention",
                type="Procedural / surgical",
                line="Complication management",
                notes="Considered for strictures, fistulas, abscesses, or refractory disease.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Crohns disease severity and phenotype are difficult to infer from claims data alone.",
            "Endoscopy, imaging, and pathology details may be incomplete or absent in administrative datasets.",
            "Biologic exposure may require combining medical and pharmacy claims to capture the full treatment journey.",
        ],
    },
    "ulcerative colitis": {
        "normalized_term": "Ulcerative Colitis",
        "aliases": ["UC", "colitis", "ulcerative colitis", "ibd uc"],
        "overview": (
            "Ulcerative colitis is a chronic inflammatory bowel disease characterized by continuous mucosal inflammation of the colon, beginning in the rectum and extending proximally to a variable extent. It typically follows a relapsing and remitting course and may range from mild distal disease to extensive colitis with systemic manifestations."
        ),
        "symptoms": [
            "Bloody diarrhea",
            "Urgency and tenesmus",
            "Abdominal pain or cramping",
            "Fatigue",
            "Weight loss in more severe disease",
        ],
        "diagnosis": [
            "Clinical history and physical examination",
            "Colonoscopy with biopsy showing continuous colonic inflammation",
            "Stool testing to exclude infectious causes",
            "Inflammatory markers and fecal calprotectin as supportive evidence",
        ],
        "icd_codes": [
            ICDCode(
                code="K51.90",
                description="Ulcerative colitis, unspecified, without complications",
            ),
        ],
        "procedures": [
            Procedure(
                name="Colonoscopy with biopsy",
                code="45380",
                indication="Diagnostic confirmation and disease assessment",
            ),
            Procedure(
                name="Flexible sigmoidoscopy",
                code="45331",
                indication="Assessment of distal disease activity when appropriate",
            ),
        ],
        "treatments": [
            Treatment(
                name="5-aminosalicylates",
                type="Pharmacological",
                line="Mild to moderate disease",
                notes="Often used for induction and maintenance in appropriate patients.",
            ),
            Treatment(
                name="Corticosteroids",
                type="Pharmacological",
                line="Induction",
                notes="Used for short-term control of active flares, not long-term maintenance.",
            ),
            Treatment(
                name="Biologic or advanced therapy",
                type="Pharmacological / biologic",
                line="Moderate to severe disease",
                notes="Used in selected patients with inadequate response or more severe disease.",
            ),
            Treatment(
                name="Colectomy",
                type="Procedural / surgical",
                line="Refractory disease / complications",
                notes="Considered for refractory disease, dysplasia, or severe complications.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [],
        "data_considerations": [
            "Ulcerative colitis extent and endoscopic severity are often not fully observable in claims data.",
            "Differentiating ulcerative colitis from Crohn's disease may require pathology, endoscopy, and longitudinal clinical context.",
            "Medication exposure may require linking pharmacy and medical claims to capture infused and self-administered therapies.",
        ],
    },
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
    "amyloidosis": {
        "normalized_term": "Amyloidosis",
        "aliases": [
            "amyloidosis",
            "al amyloidosis",
            "light chain amyloidosis",
            "attr amyloidosis",
            "transthyretin amyloidosis",
            "cardiac amyloidosis",
        ],
        "overview": (
            "Amyloidosis refers to a group of disorders caused by abnormal amyloid protein deposition in tissues and organs. "
            "Clinical presentation depends on the amyloid type and organs involved, commonly including cardiac, renal, neurologic, gastrointestinal, and soft tissue manifestations."
        ),
        "symptoms": [
            "Fatigue and weakness",
            "Shortness of breath or exercise intolerance",
            "Swelling of the legs or ankles",
            "Numbness, tingling, or neuropathic symptoms",
            "Weight loss or gastrointestinal symptoms",
        ],
        "diagnosis": [
            "Clinical evaluation based on organ involvement and suspected amyloid type",
            "Laboratory testing including monoclonal protein assessment when AL amyloidosis is suspected",
            "Tissue biopsy with amyloid confirmation and typing when appropriate",
            "Cardiac, renal, neurologic, or gastrointestinal evaluation depending on suspected organ involvement",
        ],
        "icd_codes": [
            ICDCode(code="E85.9", description="Amyloidosis, unspecified"),
            ICDCode(code="E85.81", description="Light chain (AL) amyloidosis"),
            ICDCode(
                code="E85.82", description="Wild-type transthyretin-related amyloidosis"
            ),
        ],
        "procedures": [
            Procedure(
                name="Tissue biopsy",
                code=None,
                indication="Confirmation of amyloid deposition and amyloid typing",
            ),
            Procedure(
                name="Serum and urine monoclonal protein testing",
                code=None,
                indication="Evaluation for AL amyloidosis",
            ),
            Procedure(
                name="Cardiac imaging",
                code=None,
                indication="Assessment of suspected cardiac involvement",
            ),
        ],
        "treatments": [
            Treatment(
                name="Plasma cell-directed therapy",
                type="Pharmacological",
                line="AL amyloidosis",
                notes="Used when amyloid is driven by abnormal light chain production.",
            ),
            Treatment(
                name="TTR stabilizer therapy",
                type="Pharmacological",
                line="ATTR amyloidosis",
                notes="Used in selected transthyretin amyloidosis patients depending on phenotype and indication.",
            ),
            Treatment(
                name="Supportive organ-directed care",
                type="Supportive",
                line="All types",
                notes="Management depends on cardiac, renal, neurologic, or gastrointestinal involvement.",
            ),
            Treatment(
                name="Treatment of underlying inflammatory or malignant condition",
                type="Disease-directed",
                line="Secondary amyloidosis",
                notes="Relevant when amyloidosis is driven by another condition.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="MedlinePlus Amyloidosis",
                url="https://medlineplus.gov/amyloidosis.html",
                accessed="2026-04-28",
            ),
            Source(
                name="Mayo Clinic Amyloidosis Diagnosis and Treatment",
                url="https://www.mayoclinic.org/diseases-conditions/amyloidosis/diagnosis-treatment/drc-20353183",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Amyloidosis subtype is critical but may be poorly captured in claims data.",
            "Organ involvement often requires combining diagnosis codes, procedures, labs, imaging, and specialty care patterns.",
            "AL and ATTR amyloidosis have different treatment pathways and should not be analyzed as one homogeneous population without subtype logic.",
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
            "It can be associated with systemic inflammation, comorbidities, and psoriatic arthritis in some patients."
        ),
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
            "It can involve peripheral joints, axial skeleton, entheses, digits, skin, and nails, and may lead to pain, stiffness, swelling, and structural damage if uncontrolled."
        ),
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
            "Colorectal cancer is a malignancy arising in the colon or rectum. It may develop from precancerous polyps and can present with bowel habit changes, bleeding, anemia, abdominal symptoms, or be detected through screening before symptoms occur."
        ),
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
    "celiac disease": {
        "normalized_term": "Celiac Disease",
        "aliases": [
            "celiac disease",
            "coeliac disease",
            "celiac sprue",
            "gluten sensitive enteropathy",
            "gluten-sensitive enteropathy",
        ],
        "overview": (
            "Celiac disease is a chronic immune-mediated digestive disorder triggered by gluten exposure in genetically susceptible individuals. It damages the small intestine and may cause gastrointestinal symptoms, nutrient deficiencies, and extraintestinal manifestations."
        ),
        "symptoms": [
            "Chronic diarrhea or loose stools",
            "Abdominal bloating or pain",
            "Weight loss or poor weight gain",
            "Fatigue related to anemia or nutrient deficiency",
            "Dermatitis herpetiformis or other extraintestinal symptoms",
        ],
        "diagnosis": [
            "Serologic testing for celiac-associated antibodies while the patient is consuming gluten",
            "Small intestinal biopsy to assess villous atrophy when clinically indicated",
            "Clinical and dietary history including gluten exposure",
            "Assessment for nutritional deficiencies and associated autoimmune conditions",
        ],
        "icd_codes": [
            ICDCode(code="K90.0", description="Celiac disease"),
        ],
        "procedures": [
            Procedure(
                name="Upper endoscopy with small bowel biopsy",
                code=None,
                indication="Diagnostic confirmation in selected patients",
            ),
            Procedure(
                name="Celiac serology testing",
                code=None,
                indication="Initial diagnostic evaluation and monitoring support",
            ),
            Procedure(
                name="Nutritional laboratory assessment",
                code=None,
                indication="Evaluation of deficiencies and malabsorption complications",
            ),
        ],
        "treatments": [
            Treatment(
                name="Gluten-free diet",
                type="Dietary / lifestyle",
                line="Foundational management",
                notes="Core treatment requiring long-term avoidance of gluten-containing foods.",
            ),
            Treatment(
                name="Dietitian-guided nutrition management",
                type="Supportive / nutritional",
                line="Foundational management",
                notes="Helps maintain balanced nutrition and avoid hidden gluten exposure.",
            ),
            Treatment(
                name="Correction of nutritional deficiencies",
                type="Supportive",
                line="As needed",
                notes="Used when iron, folate, vitamin D, calcium, or other deficiencies are present.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Celiac Disease",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/celiac-disease",
                accessed="2026-04-28",
            ),
            Source(
                name="NIDDK Celiac Disease Diagnosis",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/celiac-disease/diagnosis",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Claims data may capture diagnosis codes but not confirmatory serology or biopsy results.",
            "Diet adherence and gluten exposure are usually not observable in administrative data.",
            "Symptoms and nutritional deficiencies may require labs, EMR, or longitudinal clinical context.",
        ],
    },
    "nonalcoholic steatohepatitis": {
        "normalized_term": "Nonalcoholic Steatohepatitis",
        "aliases": [
            "nonalcoholic steatohepatitis",
            "nash",
            "mash",
            "metabolic dysfunction-associated steatohepatitis",
            "metabolic dysfunction associated steatohepatitis",
            "nafld",
            "masld",
        ],
        "overview": (
            "Nonalcoholic steatohepatitis is a progressive form of fatty liver disease characterized by hepatic fat accumulation with inflammation and liver cell injury. It may progress to fibrosis, cirrhosis, liver failure, or hepatocellular carcinoma in selected patients."
        ),
        "symptoms": [
            "Often asymptomatic in early disease",
            "Fatigue or low energy",
            "Right upper quadrant discomfort",
            "Signs of advanced liver disease in later stages",
            "Metabolic comorbidities such as obesity, diabetes, or dyslipidemia",
        ],
        "diagnosis": [
            "Clinical assessment of metabolic risk factors and exclusion of other liver diseases",
            "Liver enzyme and laboratory evaluation",
            "Imaging to assess hepatic steatosis and fibrosis risk",
            "Liver biopsy or noninvasive fibrosis assessment when clinically appropriate",
        ],
        "icd_codes": [
            ICDCode(code="K75.81", description="Nonalcoholic steatohepatitis (NASH)"),
            ICDCode(
                code="K76.0",
                description="Fatty change of liver, not elsewhere classified",
            ),
        ],
        "procedures": [
            Procedure(
                name="Liver imaging",
                code=None,
                indication="Assessment of steatosis, fibrosis, or cirrhosis risk",
            ),
            Procedure(
                name="Liver biopsy",
                code=None,
                indication="Definitive histologic assessment in selected patients",
            ),
            Procedure(
                name="Noninvasive fibrosis assessment",
                code=None,
                indication="Risk stratification and monitoring",
            ),
        ],
        "treatments": [
            Treatment(
                name="Weight loss and lifestyle intervention",
                type="Lifestyle / supportive",
                line="Foundational management",
                notes="Weight reduction may reduce liver fat, inflammation, and fibrosis risk.",
            ),
            Treatment(
                name="Management of metabolic comorbidities",
                type="Supportive / risk management",
                line="Foundational management",
                notes="Includes diabetes, obesity, dyslipidemia, and cardiovascular risk management.",
            ),
            Treatment(
                name="Resmetirom",
                type="Pharmacological",
                line="Selected patients",
                notes="Used in selected patients with noncirrhotic NASH/MASH with moderate to advanced liver fibrosis according to approved indication and clinical criteria.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK NAFLD and NASH",
                url="https://www.niddk.nih.gov/health-information/liver-disease/nafld-nash",
                accessed="2026-04-28",
            ),
            Source(
                name="NIDDK NAFLD and NASH Diagnosis",
                url="https://www.niddk.nih.gov/health-information/liver-disease/nafld-nash/diagnosis",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "NASH/MASH severity and fibrosis stage are often poorly captured in claims data.",
            "Diagnosis codes may underidentify patients because many cases are asymptomatic or diagnosed through labs/imaging.",
            "Linking labs, imaging, procedures, comorbidities, and medication exposure is important for real-world cohort definition.",
        ],
    },
    "sickle cell disease": {
        "normalized_term": "Sickle Cell Disease",
        "aliases": [
            "sickle cell disease",
            "scd",
            "sickle cell anemia",
            "sickle-cell disease",
            "hbss",
            "hemoglobin ss disease",
        ],
        "overview": (
            "Sickle cell disease is an inherited hemoglobin disorder characterized by abnormal sickling of red blood cells, chronic hemolytic anemia, vaso-occlusive pain episodes, and risk of multi-organ complications."
        ),
        "symptoms": [
            "Pain crises or vaso-occlusive episodes",
            "Chronic anemia and fatigue",
            "Swelling of hands or feet in some patients",
            "Recurrent infections or fever",
            "Shortness of breath or symptoms related to complications",
        ],
        "diagnosis": [
            "Hemoglobin electrophoresis or equivalent testing to identify sickle hemoglobin patterns",
            "Newborn screening or diagnostic testing based on symptoms and family history",
            "Laboratory evaluation for anemia, hemolysis, and organ complications",
            "Longitudinal assessment of pain episodes, transfusions, and complications",
        ],
        "icd_codes": [
            ICDCode(code="D57.1", description="Sickle-cell disease without crisis"),
            ICDCode(code="D57.0", description="Hb-SS disease with crisis"),
            ICDCode(code="D57.2", description="Sickle-cell/Hb-C disease"),
        ],
        "procedures": [
            Procedure(
                name="Hemoglobin electrophoresis",
                code=None,
                indication="Diagnostic confirmation and genotype characterization",
            ),
            Procedure(
                name="Blood transfusion",
                code=None,
                indication="Management or prevention of selected complications",
            ),
            Procedure(
                name="Transcranial Doppler screening",
                code=None,
                indication="Stroke risk assessment in selected pediatric patients",
            ),
        ],
        "treatments": [
            Treatment(
                name="Hydroxyurea",
                type="Pharmacological",
                line="Disease-modifying",
                notes="Used to reduce vaso-occlusive complications in selected patients.",
            ),
            Treatment(
                name="Blood transfusion therapy",
                type="Supportive / procedural",
                line="Selected complications",
                notes="Used for acute or preventive management depending on indication.",
            ),
            Treatment(
                name="Pain management and hydration",
                type="Supportive",
                line="Acute crisis management",
                notes="Used during vaso-occlusive pain episodes.",
            ),
            Treatment(
                name="Gene therapy or stem cell transplant",
                type="Cellular / gene therapy",
                line="Selected eligible patients",
                notes="Potentially disease-modifying or curative approaches for selected patients.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="CDC Sickle Cell Disease",
                url="https://www.cdc.gov/sickle-cell/index.html",
                accessed="2026-04-28",
            ),
            Source(
                name="CDC Sickle Cell Disease Prevention and Treatment",
                url="https://www.cdc.gov/sickle-cell/about/prevention-and-treatment.html",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Vaso-occlusive crises may be identified through diagnosis codes, emergency visits, inpatient stays, pain medication, or infusion encounters.",
            "Disease genotype and severity are often incompletely captured in claims data.",
            "Transfusions, hydroxyurea, gene therapy, organ complications, and acute care utilization may require longitudinal integration across care settings.",
        ],
    },
    "alpha-1 antitrypsin deficiency": {
        "normalized_term": "Alpha-1 Antitrypsin Deficiency",
        "aliases": [
            "alpha-1 antitrypsin deficiency",
            "alpha 1 antitrypsin deficiency",
            "a1at deficiency",
            "aat deficiency",
            "alpha-1",
            "alpha 1",
        ],
        "overview": (
            "Alpha-1 antitrypsin deficiency is an inherited disorder caused by low or dysfunctional alpha-1 antitrypsin protein, increasing risk of lung disease such as emphysema and liver disease in selected patients."
        ),
        "symptoms": [
            "Shortness of breath or wheezing",
            "Chronic cough",
            "Recurrent respiratory infections",
            "Reduced exercise tolerance",
            "Signs of liver disease in some patients",
        ],
        "diagnosis": [
            "Serum alpha-1 antitrypsin level testing",
            "Genotype or phenotype testing to characterize variant status",
            "Pulmonary function testing to assess lung involvement",
            "Liver evaluation when hepatic involvement is suspected",
        ],
        "icd_codes": [
            ICDCode(code="E88.01", description="Alpha-1-antitrypsin deficiency"),
        ],
        "procedures": [
            Procedure(
                name="Alpha-1 antitrypsin level testing",
                code=None,
                indication="Initial diagnostic evaluation",
            ),
            Procedure(
                name="Genotype or phenotype testing",
                code=None,
                indication="Confirmation and characterization of inherited variant",
            ),
            Procedure(
                name="Pulmonary function testing",
                code=None,
                indication="Assessment of obstructive lung disease and disease monitoring",
            ),
        ],
        "treatments": [
            Treatment(
                name="Smoking avoidance and risk reduction",
                type="Lifestyle / prevention",
                line="Foundational management",
                notes="Critical for reducing lung disease risk and progression.",
            ),
            Treatment(
                name="COPD-directed therapy",
                type="Pharmacological / supportive",
                line="Symptom and lung disease management",
                notes="Used when obstructive lung disease is present.",
            ),
            Treatment(
                name="Alpha-1 proteinase inhibitor augmentation therapy",
                type="Pharmacological / biologic",
                line="Selected patients",
                notes="Used in selected patients with emphysema related to severe deficiency according to clinical criteria.",
            ),
            Treatment(
                name="Liver disease management",
                type="Supportive / specialist care",
                line="Selected patients",
                notes="Used when hepatic involvement is present.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="MedlinePlus Alpha-1 Antitrypsin Deficiency",
                url="https://medlineplus.gov/genetics/condition/alpha-1-antitrypsin-deficiency/",
                accessed="2026-04-28",
            ),
        ],
        "data_considerations": [
            "Alpha-1 antitrypsin deficiency may be underdiagnosed and undercoded in claims data.",
            "Genotype, serum levels, smoking status, and pulmonary function values are often unavailable in administrative datasets.",
            "Augmentation therapy, COPD diagnoses, liver disease codes, and pulmonary testing can help characterize treated or clinically recognized patients.",
        ],
    },
    "gastroparesis": {
        "normalized_term": "Gastroparesis",
        "aliases": [
            "gastroparesis",
            "delayed gastric emptying",
            "gastric emptying disorder",
        ],
        "overview": (
            "Gastroparesis is a disorder of delayed stomach emptying in the absence of a mechanical blockage. "
            "It can cause chronic upper gastrointestinal symptoms and may be associated with diabetes, postsurgical states, medications, neurologic disease, or idiopathic causes."
        ),
        "symptoms": [
            "Early satiety or feeling full soon after starting a meal",
            "Nausea or vomiting",
            "Bloating or excessive belching",
            "Upper abdominal pain or discomfort",
            "Poor appetite or weight loss",
        ],
        "diagnosis": [
            "Clinical history and physical examination focused on chronic upper gastrointestinal symptoms",
            "Exclusion of mechanical obstruction with endoscopy or imaging when clinically appropriate",
            "Gastric emptying study to document delayed gastric emptying",
            "Assessment for contributing conditions such as diabetes, medications, or prior surgery",
        ],
        "icd_codes": [
            ICDCode(code="K31.84", description="Gastroparesis"),
        ],
        "procedures": [
            Procedure(
                name="Gastric emptying study",
                code=None,
                indication="Objective assessment of delayed gastric emptying",
            ),
            Procedure(
                name="Upper endoscopy",
                code=None,
                indication="Evaluation for obstruction or alternative causes of symptoms",
            ),
            Procedure(
                name="Jejunostomy tube feeding",
                code=None,
                indication="Nutritional support in selected severe cases",
            ),
        ],
        "treatments": [
            Treatment(
                name="Dietary modification",
                type="Dietary / lifestyle",
                line="Foundational management",
                notes="Small, low-fat meals and nutrition strategies are commonly used.",
            ),
            Treatment(
                name="Glucose control optimization",
                type="Supportive / metabolic",
                line="Diabetic gastroparesis",
                notes="Relevant when diabetes contributes to symptoms or delayed emptying.",
            ),
            Treatment(
                name="Prokinetic therapy",
                type="Pharmacological",
                line="Symptom management",
                notes="Used in selected patients to improve gastric motility.",
            ),
            Treatment(
                name="Antiemetic therapy",
                type="Pharmacological",
                line="Symptom management",
                notes="Used to control nausea and vomiting.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Gastroparesis",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/gastroparesis",
                accessed="2026-04-29",
            ),
            Source(
                name="NIDDK Gastroparesis Treatment",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/gastroparesis/treatment",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "Gastroparesis symptoms are often nonspecific and may overlap with functional dyspepsia, obstruction, medication effects, or other GI disorders.",
            "Claims data may capture diagnosis codes and procedures but usually lacks gastric emptying results and symptom severity.",
            "Medication exposure, diabetes status, endoscopy, gastric emptying tests, and nutrition support may help define more specific cohorts.",
        ],
    },
    "primary biliary cholangitis": {
        "normalized_term": "Primary Biliary Cholangitis",
        "aliases": [
            "primary biliary cholangitis",
            "pbc",
            "primary biliary cirrhosis",
        ],
        "overview": (
            "Primary biliary cholangitis is a chronic autoimmune cholestatic liver disease in which small intrahepatic bile ducts become injured and inflamed, leading to bile retention and potential progressive liver damage."
        ),
        "symptoms": [
            "Fatigue",
            "Pruritus or itchy skin",
            "Dry eyes or dry mouth",
            "Right upper abdominal discomfort",
            "Jaundice or complications of advanced liver disease in later stages",
        ],
        "diagnosis": [
            "Clinical evaluation with cholestatic liver enzyme pattern",
            "Serologic testing including antimitochondrial antibodies when appropriate",
            "Imaging to evaluate biliary obstruction or alternative liver disease",
            "Liver biopsy in selected cases when diagnosis is uncertain or overlap disease is suspected",
        ],
        "icd_codes": [
            ICDCode(code="K74.3", description="Primary biliary cirrhosis"),
        ],
        "procedures": [
            Procedure(
                name="Liver biochemical testing",
                code=None,
                indication="Evaluation of cholestatic liver injury",
            ),
            Procedure(
                name="Autoantibody testing",
                code=None,
                indication="Support diagnosis of primary biliary cholangitis",
            ),
            Procedure(
                name="Liver biopsy",
                code=None,
                indication="Selected cases with diagnostic uncertainty or overlap features",
            ),
        ],
        "treatments": [
            Treatment(
                name="Ursodiol",
                type="Pharmacological",
                line="First-line",
                notes="Used to slow disease progression in many patients.",
            ),
            Treatment(
                name="Second-line cholestatic liver disease therapy",
                type="Pharmacological",
                line="Inadequate response or intolerance",
                notes="Used in selected patients depending on response and indication.",
            ),
            Treatment(
                name="Pruritus management",
                type="Supportive / symptom control",
                line="As needed",
                notes="Used to manage itching and quality-of-life burden.",
            ),
            Treatment(
                name="Liver transplant",
                type="Procedural / transplant",
                line="Advanced disease",
                notes="Considered for liver failure or severe complications.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Primary Biliary Cholangitis",
                url="https://www.niddk.nih.gov/health-information/liver-disease/primary-biliary-cholangitis",
                accessed="2026-04-29",
            ),
            Source(
                name="NIDDK Primary Biliary Cholangitis Treatment",
                url="https://www.niddk.nih.gov/health-information/liver-disease/primary-biliary-cholangitis/treatment",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "PBC may be underrecognized in claims data if diagnosis codes are inconsistently used.",
            "Disease severity, biochemical response, autoantibody status, and fibrosis stage often require labs or EMR detail.",
            "Treatment persistence and response may require integration of pharmacy claims, labs, and hepatology visit patterns.",
        ],
    },
    "primary sclerosing cholangitis": {
        "normalized_term": "Primary Sclerosing Cholangitis",
        "aliases": [
            "primary sclerosing cholangitis",
            "psc",
            "sclerosing cholangitis",
        ],
        "overview": (
            "Primary sclerosing cholangitis is a chronic cholestatic liver disease characterized by inflammation, fibrosis, and narrowing of bile ducts. "
            "It is often associated with inflammatory bowel disease and may progress to cirrhosis, biliary complications, or liver transplant need."
        ),
        "symptoms": [
            "Fatigue or weakness",
            "Pruritus or itchy skin",
            "Right upper abdominal pain",
            "Jaundice",
            "Fever or symptoms of bile duct infection in selected cases",
        ],
        "diagnosis": [
            "Clinical evaluation with cholestatic liver enzyme pattern",
            "Biliary imaging such as MRCP or ERCP to evaluate bile duct strictures",
            "Assessment for inflammatory bowel disease association",
            "Liver biopsy in selected cases such as suspected small-duct disease or diagnostic uncertainty",
        ],
        "icd_codes": [
            ICDCode(code="K83.01", description="Primary sclerosing cholangitis"),
        ],
        "procedures": [
            Procedure(
                name="MRCP",
                code=None,
                indication="Noninvasive evaluation of biliary strictures and ductal changes",
            ),
            Procedure(
                name="ERCP",
                code=None,
                indication="Evaluation or management of selected dominant strictures or biliary obstruction",
            ),
            Procedure(
                name="Colonoscopy",
                code=None,
                indication="Evaluation or surveillance for associated inflammatory bowel disease",
            ),
        ],
        "treatments": [
            Treatment(
                name="Management of biliary strictures",
                type="Procedural / supportive",
                line="Complication management",
                notes="Used for selected narrowed or blocked bile ducts.",
            ),
            Treatment(
                name="Pruritus management",
                type="Supportive / symptom control",
                line="As needed",
                notes="Used for itching and quality-of-life burden.",
            ),
            Treatment(
                name="Cholangitis management",
                type="Supportive / antimicrobial",
                line="Complication management",
                notes="Used when bile duct infection is suspected or confirmed.",
            ),
            Treatment(
                name="Liver transplant",
                type="Procedural / transplant",
                line="Advanced disease",
                notes="Considered for liver failure, recurrent cholangitis, or severe complications.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Primary Sclerosing Cholangitis",
                url="https://www.niddk.nih.gov/health-information/liver-disease/primary-sclerosing-cholangitis",
                accessed="2026-04-29",
            ),
            Source(
                name="NIDDK Primary Sclerosing Cholangitis Treatment",
                url="https://www.niddk.nih.gov/health-information/liver-disease/primary-sclerosing-cholangitis/treatment",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "PSC is rare and cohort definitions may need diagnosis codes plus hepatology care, biliary imaging, ERCP, or IBD context.",
            "Claims data usually lacks bile duct imaging findings, liver biochemistry trends, and disease stage.",
            "Associated IBD, cholangitis, biliary procedures, transplant evaluation, and malignancy surveillance are important longitudinal signals.",
        ],
    },
    "chronic pancreatitis": {
        "normalized_term": "Chronic Pancreatitis",
        "aliases": [
            "chronic pancreatitis",
            "cp pancreatitis",
            "recurrent chronic pancreatitis",
            "pancreatic insufficiency chronic pancreatitis",
        ],
        "overview": (
            "Chronic pancreatitis is a long-standing inflammatory disease of the pancreas that can lead to irreversible structural damage, chronic abdominal pain, exocrine pancreatic insufficiency, diabetes, and nutritional complications."
        ),
        "symptoms": [
            "Chronic or recurrent upper abdominal pain",
            "Nausea or digestive discomfort",
            "Steatorrhea or fatty stools",
            "Weight loss or malnutrition",
            "Diabetes or glucose intolerance in advanced disease",
        ],
        "diagnosis": [
            "Clinical history including recurrent pancreatitis, alcohol exposure, smoking, genetic risk, or obstructive causes",
            "Pancreatic imaging to assess calcifications, ductal changes, or structural damage",
            "Assessment for exocrine pancreatic insufficiency and nutritional deficiencies",
            "Evaluation for diabetes or endocrine pancreatic dysfunction",
        ],
        "icd_codes": [
            ICDCode(code="K86.1", description="Other chronic pancreatitis"),
            ICDCode(code="K86.0", description="Alcohol-induced chronic pancreatitis"),
        ],
        "procedures": [
            Procedure(
                name="Pancreatic imaging",
                code=None,
                indication="Evaluation of structural pancreatic damage",
            ),
            Procedure(
                name="Endoscopic pancreatic intervention",
                code=None,
                indication="Selected cases with ductal obstruction or complications",
            ),
            Procedure(
                name="Fecal elastase testing",
                code=None,
                indication="Evaluation for exocrine pancreatic insufficiency",
            ),
        ],
        "treatments": [
            Treatment(
                name="Pain management",
                type="Supportive / pharmacological",
                line="Symptom control",
                notes="Used for chronic or recurrent abdominal pain.",
            ),
            Treatment(
                name="Pancreatic enzyme replacement therapy",
                type="Pharmacological / digestive support",
                line="Exocrine insufficiency",
                notes="Used when malabsorption or pancreatic enzyme insufficiency is present.",
            ),
            Treatment(
                name="Alcohol and smoking cessation",
                type="Lifestyle / risk reduction",
                line="Foundational management",
                notes="Important for reducing progression and complications.",
            ),
            Treatment(
                name="Endoscopic or surgical management",
                type="Procedural",
                line="Selected complications",
                notes="Considered for obstructive disease, ductal complications, or refractory symptoms.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Pancreatitis",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/pancreatitis",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "Chronic pancreatitis may require repeated diagnosis codes, imaging/procedure signals, and longitudinal pain or enzyme therapy patterns.",
            "Alcohol, smoking, genetic risk, imaging findings, and severity are often incomplete in claims data.",
            "Exocrine pancreatic insufficiency and diabetes complications may require linked labs, prescriptions, and encounter patterns.",
        ],
    },
    "eosinophilic esophagitis": {
        "normalized_term": "Eosinophilic Esophagitis",
        "aliases": [
            "eosinophilic esophagitis",
            "eoe",
            "eosinophilic oesophagitis",
            "allergic esophagitis",
        ],
        "overview": (
            "Eosinophilic esophagitis is a chronic immune-mediated inflammatory disease of the esophagus characterized by eosinophil-predominant inflammation and symptoms of esophageal dysfunction."
        ),
        "symptoms": [
            "Difficulty swallowing or dysphagia",
            "Food impaction",
            "Chest discomfort or heartburn-like symptoms",
            "Abdominal pain, vomiting, or feeding difficulty in children",
            "Avoidance of certain foods or slow eating behaviors",
        ],
        "diagnosis": [
            "Clinical history of esophageal dysfunction or food impaction",
            "Upper endoscopy with esophageal biopsies",
            "Histologic evaluation showing eosinophil-predominant inflammation",
            "Assessment for alternative causes of esophageal eosinophilia",
        ],
        "icd_codes": [
            ICDCode(code="K20.0", description="Eosinophilic esophagitis"),
        ],
        "procedures": [
            Procedure(
                name="Upper endoscopy with esophageal biopsy",
                code=None,
                indication="Diagnostic confirmation and assessment of esophageal inflammation",
            ),
            Procedure(
                name="Esophageal dilation",
                code=None,
                indication="Selected patients with strictures or narrowing",
            ),
            Procedure(
                name="Allergy or dietary assessment",
                code=None,
                indication="Support management planning in selected patients",
            ),
        ],
        "treatments": [
            Treatment(
                name="Proton pump inhibitor therapy",
                type="Pharmacological",
                line="Initial or selected management",
                notes="Used in selected patients with esophageal eosinophilia and symptoms.",
            ),
            Treatment(
                name="Swallowed topical corticosteroids",
                type="Pharmacological",
                line="Anti-inflammatory therapy",
                notes="Used to reduce esophageal inflammation.",
            ),
            Treatment(
                name="Dietary elimination therapy",
                type="Dietary / lifestyle",
                line="Selected patients",
                notes="Used to identify and avoid dietary triggers in selected patients.",
            ),
            Treatment(
                name="Biologic therapy",
                type="Pharmacological / biologic",
                line="Selected patients",
                notes="Used in selected patients with persistent or severe disease based on indication and clinical criteria.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Eosinophilic Esophagitis",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/eosinophilic-esophagitis",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "EoE diagnosis ideally requires endoscopy and biopsy detail, which may not be available in claims data.",
            "Food impaction, repeated endoscopies, dilation, PPI use, topical steroid use, and biologic exposure can help characterize disease burden.",
            "Pediatric and adult presentation may differ, so age-specific cohort logic may be needed.",
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
