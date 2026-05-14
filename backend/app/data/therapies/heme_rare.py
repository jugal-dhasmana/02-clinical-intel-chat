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

THERAPIES_HEME_RARE = {
    "ittp": {
        "normalized_term": "Immune Thrombotic Thrombocytopenic Purpura",
        "aliases": [
            "iTTP",
            "ttp",
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
        "diagnostic_considerations": [
            "iTTP should be suspected in patients with thrombocytopenia and microangiopathic hemolytic anemia without an alternative explanation.",
            "Severe ADAMTS13 deficiency, typically below 10%, strongly supports the diagnosis of immune-mediated TTP.",
            "Because ADAMTS13 testing may not be immediately available, treatment is often initiated based on clinical suspicion before confirmatory results return.",
            "PLASMIC and related clinical scoring systems may support early risk stratification in suspected thrombotic microangiopathy.",
            "Diagnostic evaluation commonly includes exclusion of other thrombotic microangiopathies and secondary causes such as hemolytic uremic syndrome, disseminated intravascular coagulation, severe hypertension, infection, malignancy, or drug-induced thrombotic microangiopathy.",
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
}
