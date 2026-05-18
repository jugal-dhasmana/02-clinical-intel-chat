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
            "Immune thrombotic thrombocytopenic purpura is a rare, life-threatening thrombotic microangiopathy caused by severe ADAMTS13 deficiency, usually due to acquired autoantibodies. "
            "It is characterized by thrombocytopenia, microangiopathic hemolytic anemia, and risk of neurologic, cardiac, renal, and other organ ischemia, requiring urgent recognition and treatment.\n\n"
            "Global / U.S. Epidemiology: iTTP is rare, with reported annual incidence generally estimated at approximately 2 to 6 cases per million people globally. "
            "U.S. real-world estimates have reported annual iTTP episode incidence around 1.8 to 3.4 per million, depending on case definition and data source."
        ),
        "causes": [
            "Severe acquired deficiency of ADAMTS13 activity caused by autoantibodies against the ADAMTS13 enzyme.",
            "Deficiency of ADAMTS13 leads to accumulation of ultra-large von Willebrand factor multimers and platelet-rich microvascular thrombosis.",
        ],
        "risk_factors": [
            "Female sex",
            "History of autoimmune disease",
            "Pregnancy or postpartum state",
            "HIV infection",
            "Certain medications associated with thrombotic microangiopathy",
        ],
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
        "overview": (
            "Multiple myeloma is a plasma cell malignancy characterized by clonal proliferation in the bone marrow and end-organ damage in selected patients. "
            "Disease manifestations commonly involve bone destruction, anemia, renal dysfunction, hypercalcemia, and immunologic impairment.\n\n"
            "Global / U.S. Epidemiology: Multiple myeloma accounts for approximately 1% to 2% of all cancers and about 10% of hematologic malignancies. "
            "U.S. prevalence is estimated at more than 150,000 people living with multiple myeloma."
        ),
        "causes": [
            "Clonal proliferation of malignant plasma cells within the bone marrow.",
            "Disease biology involves abnormal plasma cell growth, monoclonal protein production, immune dysregulation, and bone marrow microenvironment interactions.",
        ],
        "risk_factors": [
            "Older age",
            "Male sex",
            "African ancestry",
            "Family history of plasma cell disorders",
            "Monoclonal gammopathy of undetermined significance (MGUS)",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis integrates monoclonal protein testing, bone marrow plasma cell evaluation, imaging, and assessment of end-organ involvement.",
            "CRAB criteria and myeloma-defining events are important for distinguishing symptomatic disease from precursor states.",
            "Differential diagnosis includes MGUS, smoldering myeloma, plasmacytoma, amyloidosis, and other plasma cell disorders.",
            "Disease staging and cytogenetic risk assessment influence prognosis and treatment strategy.",
            "In real-world data, cytogenetics, bone marrow findings, staging, and disease response assessments are often incompletely captured.",
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
            "Hemophilia A is an inherited bleeding disorder caused by deficiency or dysfunction of coagulation factor VIII, resulting in impaired blood clotting and increased bleeding risk. "
            "Severity varies based on factor VIII activity level and may range from mild bleeding tendency to spontaneous joint and muscle hemorrhage.\n\n"
            "Global / U.S. Epidemiology: Hemophilia A occurs worldwide and is one of the most common inherited bleeding disorders. "
            "Global prevalence is commonly estimated at approximately 15 to 20 cases per 100,000 males, while U.S. estimates suggest more than 20,000 individuals are living with hemophilia A."
        ),
        "causes": [
            "Inherited mutation in the F8 gene resulting in reduced or absent factor VIII activity.",
            "Most cases follow X-linked inheritance, although spontaneous mutations can occur.",
        ],
        "risk_factors": [
            "Family history of hemophilia",
            "Male sex due to X-linked inheritance pattern",
            "Known maternal carrier status",
            "Personal or family history of unexplained bleeding disorders",
        ],
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
        "diagnostic_considerations": [
            "Hemophilia A diagnosis is based on reduced factor VIII activity in the setting of compatible bleeding history and clinical presentation.",
            "Disease severity is commonly classified by factor VIII activity level and may influence bleeding risk, treatment intensity, and prophylaxis strategy.",
            "Differential diagnosis may include other inherited or acquired coagulation disorders, including von Willebrand disease and acquired factor inhibitors.",
            "Inhibitor development is an important clinical consideration because neutralizing antibodies against factor VIII can significantly alter treatment response.",
            "In real-world data, disease severity, inhibitor status, bleeding frequency, and prophylaxis adherence are often incompletely captured in claims datasets.",
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
            "Clinical presentation depends on amyloid subtype and organs involved, commonly including cardiac, renal, neurologic, gastrointestinal, and soft tissue manifestations.\n\n"
            "Global / U.S. Epidemiology: Amyloidosis is rare, although recognition has increased with improved diagnostic techniques. "
            "ATTR amyloidosis prevalence appears to be increasing, particularly among older adults and patients with cardiomyopathy."
        ),
        "causes": [
            "Misfolded protein deposition within tissues and organs resulting in amyloid accumulation and organ dysfunction.",
            "Amyloid subtype may be related to plasma cell disorders, transthyretin instability, chronic inflammation, or hereditary mutations.",
        ],
        "risk_factors": [
            "Older age",
            "Monoclonal plasma cell disorders",
            "Family history of hereditary amyloidosis",
            "Chronic inflammatory conditions",
            "Male sex in some ATTR amyloidosis populations",
        ],
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
        "diagnostic_considerations": [
            "Accurate amyloid subtype identification is critical because treatment pathways differ substantially between AL, ATTR, and secondary amyloidosis.",
            "Diagnosis often requires tissue confirmation together with specialized amyloid typing techniques.",
            "Cardiac involvement may mimic hypertrophic or restrictive cardiomyopathy and is increasingly recognized in older adults.",
            "Monoclonal protein evaluation is important when AL amyloidosis is suspected.",
            "In real-world data, amyloid subtype, organ involvement, biopsy findings, and staging details are often incompletely captured.",
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
            "Sickle cell disease is an inherited hemoglobin disorder characterized by abnormal sickling of red blood cells, chronic hemolytic anemia, vaso-occlusive pain episodes, and risk of multi-organ complications.\n\n"
            "Global / U.S. Epidemiology: Sickle cell disease affects millions of people globally and is particularly prevalent among individuals of African ancestry. "
            "Approximately 100,000 individuals are estimated to live with sickle cell disease in the United States."
        ),
        "causes": [
            "Inherited mutation in the beta-globin gene resulting in abnormal hemoglobin S formation.",
            "Red blood cell sickling contributes to vaso-occlusion, hemolysis, inflammation, and organ injury.",
        ],
        "risk_factors": [
            "Family history of sickle cell disease or sickle cell trait",
            "African, Mediterranean, Middle Eastern, or South Asian ancestry",
            "Inheritance of two abnormal beta-globin genes",
        ],
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
        "diagnostic_considerations": [
            "Hemoglobin electrophoresis or equivalent testing is central to diagnostic confirmation and genotype characterization.",
            "Disease severity varies substantially by genotype and clinical phenotype.",
            "Acute complications may include vaso-occlusive crises, acute chest syndrome, stroke, and infection-related morbidity.",
            "Longitudinal monitoring of organ complications and transfusion exposure is important.",
            "In real-world data, genotype, disease severity, and acute complication detail may be incompletely captured.",
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
            "Alpha-1 antitrypsin deficiency is an inherited disorder caused by low or dysfunctional alpha-1 antitrypsin protein, increasing risk of lung disease such as emphysema and liver disease in selected patients.\n\n"
            "Global / U.S. Epidemiology: Alpha-1 antitrypsin deficiency is considered underdiagnosed worldwide. "
            "Severe deficiency genotypes are estimated to affect approximately 1 in 2,000 to 1 in 5,000 individuals in populations of European ancestry."
        ),
        "causes": [
            "Inherited SERPINA1 gene mutations resulting in low or dysfunctional alpha-1 antitrypsin protein.",
            "Protein deficiency increases risk of protease-mediated lung injury and abnormal protein accumulation in the liver.",
        ],
        "risk_factors": [
            "Family history of alpha-1 antitrypsin deficiency",
            "Smoking exposure",
            "European ancestry in some severe deficiency populations",
            "Underlying chronic lung disease or emphysema at younger age",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis involves alpha-1 antitrypsin level assessment together with genotype or phenotype testing.",
            "Testing should be considered in early emphysema, unexplained liver disease, or family history of deficiency.",
            "Smoking exposure substantially accelerates lung disease progression.",
            "Liver involvement may occur independently of lung disease severity.",
            "In real-world data, genotype detail, pulmonary function testing, smoking status, and augmentation eligibility are often incompletely captured.",
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
    "narcolepsy type 1": {
        "normalized_term": "Narcolepsy Type 1",
        "aliases": [
            "nt1",
            "narcolepsy type 1",
            "type 1 narcolepsy",
            "narcolepsy with cataplexy",
            "cataplexy narcolepsy",
            "orexin deficiency",
            "hypocretin deficiency",
        ],
        "overview": (
            "Narcolepsy Type 1 is a chronic neurologic sleep disorder characterized by excessive daytime sleepiness and cataplexy, often associated with loss of hypocretin/orexin signaling. "
            "It affects sleep-wake regulation and may include disrupted nighttime sleep, sleep paralysis, and hallucinations around sleep transitions.\n\n"
            "Global / U.S. Epidemiology: Narcolepsy is rare worldwide, with prevalence estimates commonly ranging from approximately 25 to 50 cases per 100,000 people. "
            "Narcolepsy Type 1 represents the subtype associated with cataplexy and hypocretin deficiency."
        ),
        "causes": [
            "Loss or dysfunction of hypocretin/orexin-producing neurons involved in sleep-wake regulation.",
            "Narcolepsy Type 1 is commonly associated with autoimmune-mediated hypocretin deficiency, although exact mechanisms may vary.",
        ],
        "risk_factors": [
            "Family history of narcolepsy",
            "Certain HLA genetic associations such as HLA-DQB1*06:02",
            "Autoimmune susceptibility",
            "History of cataplexy or symptoms beginning in adolescence or young adulthood",
            "Possible environmental triggers in genetically susceptible individuals",
        ],
        "symptoms": [
            "Excessive daytime sleepiness",
            "Cataplexy or sudden loss of muscle tone triggered by emotion",
            "Sleep paralysis",
            "Hypnagogic or hypnopompic hallucinations",
            "Fragmented nighttime sleep",
        ],
        "diagnosis": [
            "Clinical history of excessive daytime sleepiness and cataplexy",
            "Overnight polysomnography followed by multiple sleep latency testing",
            "Short mean sleep latency with sleep-onset REM periods on MSLT",
            "Low cerebrospinal fluid hypocretin-1 level when tested",
        ],
        "diagnostic_considerations": [
            "Narcolepsy Type 1 is distinguished from Narcolepsy Type 2 primarily by cataplexy and/or hypocretin deficiency.",
            "Diagnostic evaluation should exclude insufficient sleep, obstructive sleep apnea, circadian rhythm disorders, medication effects, and other hypersomnolence disorders.",
            "MSLT interpretation may be affected by sleep deprivation, antidepressants, stimulants, REM-suppressing medications, and untreated sleep disorders.",
            "Cataplexy history is clinically important and may be underdocumented in routine claims or EMR data.",
            "In real-world data, narcolepsy subtype may be difficult to distinguish unless cataplexy codes, sleep study evidence, specialist care, or medication patterns are available.",
        ],
        "icd_codes": [
            ICDCode(code="G47.411", description="Narcolepsy with cataplexy"),
        ],
        "procedures": [
            Procedure(
                name="Polysomnography",
                code=None,
                indication="Overnight sleep assessment before MSLT and evaluation for other sleep disorders",
            ),
            Procedure(
                name="Multiple sleep latency test",
                code=None,
                indication="Objective assessment of daytime sleepiness and sleep-onset REM periods",
            ),
            Procedure(
                name="CSF hypocretin-1 testing",
                code=None,
                indication="Support diagnostic confirmation when hypocretin deficiency is suspected",
            ),
        ],
        "treatments": [
            Treatment(
                name="Wake-promoting therapy",
                type="Pharmacological",
                line="Daytime sleepiness management",
                notes="Used to improve excessive daytime sleepiness in selected patients.",
            ),
            Treatment(
                name="Sodium oxybate or oxybate therapy",
                type="Pharmacological",
                line="Cataplexy and sleepiness management",
                notes="Used in selected patients to reduce cataplexy and improve sleep-related symptoms.",
            ),
            Treatment(
                name="Antidepressant therapy",
                type="Pharmacological",
                line="Cataplexy symptom management",
                notes="Some REM-suppressing agents may be used to reduce cataplexy in selected patients.",
            ),
            Treatment(
                name="Behavioral and safety strategies",
                type="Supportive",
                line="Foundational management",
                notes="Includes scheduled naps, sleep hygiene, driving safety counseling, and school or workplace accommodations.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NINDS Narcolepsy",
                url="https://www.ninds.nih.gov/health-information/disorders/narcolepsy",
                accessed="2026-05-18",
            ),
            Source(
                name="NCBI Bookshelf Narcolepsy",
                url="https://www.ncbi.nlm.nih.gov/books/NBK459236/",
                accessed="2026-05-18",
            ),
            Source(
                name="ICD-10-CM G47.411 Narcolepsy with cataplexy",
                url="https://www.icd10data.com/ICD10CM/Codes/G00-G99/G40-G47/G47-/G47.411",
                accessed="2026-05-18",
            ),
        ],
        "data_considerations": [
            "Claims data may identify narcolepsy but often lacks sleep study results, MSLT metrics, and hypocretin testing.",
            "Cataplexy may be undercoded, making Narcolepsy Type 1 difficult to distinguish from Narcolepsy Type 2.",
            "Medication patterns may support phenotype identification but are not specific because wake-promoting agents can be used across multiple sleep disorders.",
            "Specialist visits, sleep study procedures, diagnosis persistence, and cataplexy documentation can improve cohort specificity.",
        ],
    },
    "polycythemia vera": {
        "normalized_term": "Polycythemia Vera",
        "aliases": [
            "pv",
            "polycythemia vera",
            "polycythaemia vera",
            "primary polycythemia",
            "primary polycythaemia",
            "jak2 polycythemia",
            "myeloproliferative neoplasm polycythemia vera",
        ],
        "overview": (
            "Polycythemia vera is a chronic myeloproliferative neoplasm characterized by increased red blood cell production, often associated with JAK2 mutation. "
            "It can increase blood viscosity and is associated with thrombotic risk, symptoms such as pruritus or headache, and potential progression to myelofibrosis or acute leukemia in some patients.\n\n"
            "Global / U.S. Epidemiology: Polycythemia vera is a rare hematologic malignancy with reported prevalence commonly ranging from approximately 20 to 60 cases per 100,000 people in North America and Europe."
        ),
        "causes": [
            "Clonal myeloproliferation leading to increased red blood cell production.",
            "Most cases are associated with acquired JAK2 mutation, commonly JAK2 V617F or exon 12 mutation.",
        ],
        "risk_factors": [
            "Older age",
            "JAK2 mutation positivity",
            "History of thrombosis",
            "Cardiovascular risk factors such as hypertension, diabetes, smoking, or hyperlipidemia",
            "Male sex in some epidemiologic studies",
        ],
        "symptoms": [
            "Headache, dizziness, or visual disturbances",
            "Aquagenic pruritus or itching after warm water exposure",
            "Fatigue or weakness",
            "Erythromelalgia or burning pain and redness in hands or feet",
            "Splenomegaly or abdominal fullness",
        ],
        "diagnosis": [
            "CBC showing elevated hemoglobin, hematocrit, or red cell mass",
            "JAK2 mutation testing",
            "Serum erythropoietin level, often low in PV",
            "Bone marrow evaluation when needed to support diagnosis and assess myeloproliferative features",
        ],
        "diagnostic_considerations": [
            "Polycythemia vera should be distinguished from secondary erythrocytosis due to hypoxia, smoking, sleep apnea, testosterone use, renal disease, or erythropoietin-producing tumors.",
            "JAK2 mutation status is central to diagnostic evaluation, but laboratory values and clinical context are also important.",
            "Thrombotic risk assessment is important and often incorporates age, prior thrombosis, cardiovascular risk factors, and hematocrit control.",
            "Hematocrit control is a key treatment target because elevated hematocrit is associated with increased thrombotic risk.",
            "In real-world data, PV may be confused with secondary polycythemia unless diagnosis persistence, hematology care, JAK2 testing, phlebotomy, cytoreductive therapy, and lab patterns are considered.",
        ],
        "icd_codes": [
            ICDCode(code="D45", description="Polycythemia vera"),
        ],
        "procedures": [
            Procedure(
                name="JAK2 mutation testing",
                code=None,
                indication="Support diagnostic confirmation of polycythemia vera",
            ),
            Procedure(
                name="Therapeutic phlebotomy",
                code=None,
                indication="Reduce hematocrit and blood viscosity in selected patients",
            ),
            Procedure(
                name="Bone marrow biopsy",
                code=None,
                indication="Support diagnosis and evaluate marrow morphology when clinically appropriate",
            ),
        ],
        "treatments": [
            Treatment(
                name="Therapeutic phlebotomy",
                type="Procedural",
                line="Foundational management",
                notes="Used to reduce hematocrit, commonly targeting hematocrit below 45% in appropriate patients.",
            ),
            Treatment(
                name="Low-dose aspirin",
                type="Pharmacological",
                line="Thrombosis risk reduction",
                notes="Used in many patients unless contraindicated.",
            ),
            Treatment(
                name="Cytoreductive therapy",
                type="Pharmacological",
                line="High-risk or selected patients",
                notes="Hydroxyurea or interferon-based therapy may be used depending on patient risk and clinical context.",
            ),
            Treatment(
                name="JAK inhibitor therapy",
                type="Pharmacological / targeted therapy",
                line="Selected patients",
                notes="Ruxolitinib may be used in selected patients with inadequate response or intolerance to hydroxyurea.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NCI Myeloproliferative Neoplasms Treatment PDQ",
                url="https://www.cancer.gov/types/myeloproliferative/hp/myeloproliferative-neoplasms-treatment",
                accessed="2026-05-18",
            ),
            Source(
                name="Merck Manual Professional Polycythemia Vera",
                url="https://www.merckmanuals.com/professional/hematology-and-oncology/myeloproliferative-disorders/polycythemia-vera",
                accessed="2026-05-18",
            ),
            Source(
                name="ICD-10-CM D45 Polycythemia vera",
                url="https://www.icd10data.com/ICD10CM/Codes/C00-D49/D37-D48/D45-/D45",
                accessed="2026-05-18",
            ),
        ],
        "data_considerations": [
            "Claims data may identify PV diagnosis but usually lacks complete hematocrit, hemoglobin, erythropoietin, and JAK2 test results unless linked labs are available.",
            "Secondary erythrocytosis can create false positives if cohort logic relies on diagnosis codes alone.",
            "Phlebotomy, hematology visits, cytoreductive therapy, aspirin use, thrombotic events, and serial CBC values may help strengthen real-world cohort definitions.",
            "Risk stratification variables such as prior thrombosis, cardiovascular risk factors, symptom burden, and hematocrit control may require longitudinal claims, labs, and EMR integration.",
        ],
    },
}
