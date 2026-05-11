from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_GI_ONCOLOGY = {
    "irritable bowel syndrome": {
        "normalized_term": "Irritable Bowel Syndrome",
        "aliases": ["ibs", "irritable bowel syndrome", "spastic colon"],
        "overview": (
            "Irritable bowel syndrome is a chronic disorder of gut-brain interaction characterized by recurrent abdominal pain "
            "associated with altered bowel habits, including diarrhea, constipation, or mixed patterns."
        ),
        "symptoms": [
            "Recurrent abdominal pain",
            "Bloating or abdominal distension",
            "Diarrhea, constipation, or mixed bowel habits",
            "Mucus in stool in some patients",
            "Symptoms that may fluctuate over time",
        ],
        "diagnosis": [
            "Clinical evaluation based on symptom pattern and duration",
            "Assessment for alarm features such as bleeding, weight loss, anemia, or nocturnal symptoms",
            "Limited testing to exclude alternative diagnoses when clinically appropriate",
            "Classification by predominant bowel habit such as IBS-D, IBS-C, or IBS-M",
        ],
        "icd_codes": [
            ICDCode(
                code="K58.9", description="Irritable bowel syndrome without diarrhea"
            ),
            ICDCode(code="K58.0", description="Irritable bowel syndrome with diarrhea"),
        ],
        "procedures": [
            Procedure(
                name="Clinical evaluation",
                code=None,
                indication="Symptom-based assessment and exclusion of alarm features",
            ),
            Procedure(
                name="Colonoscopy",
                code=None,
                indication="Selected patients with alarm features or screening indications",
            ),
        ],
        "treatments": [
            Treatment(
                name="Dietary modification",
                type="Dietary / lifestyle",
                line="Foundational management",
                notes="May include fiber adjustment or low-FODMAP strategy in selected patients.",
            ),
            Treatment(
                name="Antidiarrheal or laxative therapy",
                type="Pharmacological",
                line="Symptom-directed",
                notes="Selected based on diarrhea-predominant or constipation-predominant symptoms.",
            ),
            Treatment(
                name="Gut-brain neuromodulator therapy",
                type="Pharmacological",
                line="Selected patients",
                notes="Used when pain, visceral sensitivity, or persistent symptoms are prominent.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Irritable Bowel Syndrome",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "IBS is symptom-defined, so claims data may not capture diagnostic certainty or subtype accurately.",
            "IBS-D, IBS-C, and IBS-M may require medication, diagnosis, and symptom proxy logic.",
            "Exclusion of inflammatory bowel disease, celiac disease, malignancy, or infection may be important for cohort specificity.",
        ],
    },
    "exocrine pancreatic insufficiency": {
        "normalized_term": "Exocrine Pancreatic Insufficiency",
        "aliases": [
            "epi",
            "exocrine pancreatic insufficiency",
            "pancreatic insufficiency",
        ],
        "overview": (
            "Exocrine pancreatic insufficiency is a condition in which inadequate pancreatic enzyme activity leads to impaired digestion "
            "and malabsorption, often associated with chronic pancreatitis, pancreatic surgery, cystic fibrosis, or pancreatic cancer."
        ),
        "symptoms": [
            "Steatorrhea or oily foul-smelling stools",
            "Weight loss or poor weight gain",
            "Bloating or excessive gas",
            "Abdominal discomfort",
            "Fat-soluble vitamin deficiencies in some patients",
        ],
        "diagnosis": [
            "Clinical evaluation of malabsorption symptoms and risk factors",
            "Fecal elastase or other pancreatic function testing when available",
            "Assessment for underlying causes such as chronic pancreatitis or pancreatic surgery",
            "Nutritional evaluation for weight loss and vitamin deficiencies",
        ],
        "icd_codes": [
            ICDCode(code="K86.81", description="Exocrine pancreatic insufficiency"),
        ],
        "procedures": [
            Procedure(
                name="Fecal elastase testing",
                code=None,
                indication="Support diagnosis of pancreatic enzyme insufficiency",
            ),
            Procedure(
                name="Nutritional laboratory assessment",
                code=None,
                indication="Assess malabsorption and vitamin deficiency burden",
            ),
            Procedure(
                name="Pancreatic imaging",
                code=None,
                indication="Evaluate underlying pancreatic disease",
            ),
        ],
        "treatments": [
            Treatment(
                name="Pancreatic enzyme replacement therapy",
                type="Pharmacological / digestive support",
                line="Foundational management",
                notes="Core treatment for enzyme replacement.",
            ),
            Treatment(
                name="Nutritional support",
                type="Supportive / nutritional",
                line="As needed",
                notes="Used for weight loss, malnutrition, or vitamin deficiencies.",
            ),
            Treatment(
                name="Lifestyle modification",
                type="Lifestyle / risk reduction",
                line="Supportive",
                notes="May include alcohol avoidance, smoking cessation, and dietary optimization.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Exocrine Pancreatic Insufficiency",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/exocrine-pancreatic-insufficiency",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "EPI diagnosis may be undercoded and may require PERT exposure as a supporting signal.",
            "Claims data usually lacks fecal elastase values and nutritional status details.",
            "Underlying cause should be captured where possible because EPI from chronic pancreatitis, pancreatic cancer, or surgery may represent different populations.",
        ],
    },
    "gastroesophageal reflux disease": {
        "normalized_term": "Gastroesophageal Reflux Disease",
        "aliases": [
            "gerd",
            "gastroesophageal reflux disease",
            "acid reflux",
            "reflux disease",
        ],
        "overview": (
            "Gastroesophageal reflux disease is a chronic condition in which stomach contents reflux into the esophagus and cause bothersome symptoms "
            "or complications such as esophagitis, stricture, or Barrett's esophagus."
        ),
        "symptoms": [
            "Heartburn",
            "Regurgitation of stomach contents",
            "Chest discomfort related to reflux",
            "Difficulty swallowing in selected patients",
            "Chronic cough or hoarseness in some patients",
        ],
        "diagnosis": [
            "Clinical evaluation based on symptoms and medical history",
            "Empiric acid suppression trial in selected patients",
            "Upper endoscopy when alarm features or complications are suspected",
            "Ambulatory reflux monitoring in selected uncertain or refractory cases",
        ],
        "icd_codes": [
            ICDCode(
                code="K21.9",
                description="Gastro-esophageal reflux disease without esophagitis",
            ),
            ICDCode(
                code="K21.0",
                description="Gastro-esophageal reflux disease with esophagitis",
            ),
        ],
        "procedures": [
            Procedure(
                name="Upper endoscopy",
                code=None,
                indication="Evaluate esophagitis, stricture, Barrett's esophagus, or alarm features",
            ),
            Procedure(
                name="Ambulatory pH monitoring",
                code=None,
                indication="Selected patients with uncertain or refractory symptoms",
            ),
        ],
        "treatments": [
            Treatment(
                name="Lifestyle modification",
                type="Lifestyle / supportive",
                line="Foundational management",
                notes="Includes weight management, meal timing, and trigger avoidance when relevant.",
            ),
            Treatment(
                name="Proton pump inhibitor therapy",
                type="Pharmacological",
                line="Common first-line pharmacologic therapy",
                notes="Used to reduce acid exposure and heal esophagitis.",
            ),
            Treatment(
                name="H2 receptor antagonist therapy",
                type="Pharmacological",
                line="Selected patients",
                notes="Used for symptom control in selected cases.",
            ),
            Treatment(
                name="Antireflux surgery or endoscopic therapy",
                type="Procedural",
                line="Selected refractory or complicated disease",
                notes="Considered for selected patients.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK GERD Diagnosis",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/acid-reflux-ger-gerd-adults/diagnosis",
                accessed="2026-04-29",
            ),
            Source(
                name="NIDDK GERD Treatment",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/acid-reflux-ger-gerd-adults/treatment",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "GERD is common and diagnosis codes alone may have low specificity for clinically meaningful disease.",
            "Medication use may include over-the-counter therapy not fully captured in claims.",
            "Complicated GERD may require endoscopy, esophagitis, stricture, Barrett's esophagus, or procedure signals.",
        ],
    },
    "barretts esophagus": {
        "normalized_term": "Barrett's Esophagus",
        "aliases": [
            "barretts esophagus",
            "barrett's esophagus",
            "barrett esophagus",
            "barrett oesophagus",
        ],
        "overview": (
            "Barrett's esophagus is a condition in which the lining of the esophagus changes, usually in the setting of chronic gastroesophageal reflux. "
            "It is clinically important because it is associated with increased risk of esophageal adenocarcinoma."
        ),
        "symptoms": [
            "Often asymptomatic itself",
            "Heartburn symptoms related to GERD",
            "Regurgitation related to GERD",
            "Difficulty swallowing in selected patients",
            "Chest discomfort or chronic cough in some patients",
        ],
        "diagnosis": [
            "Upper GI endoscopy with visualization of suspected Barrett's mucosa",
            "Biopsy confirmation of intestinal metaplasia when clinically appropriate",
            "Assessment for dysplasia status",
            "Risk stratification based on GERD history, endoscopic findings, and pathology",
        ],
        "icd_codes": [
            ICDCode(code="K22.70", description="Barrett's esophagus without dysplasia"),
            ICDCode(code="K22.71", description="Barrett's esophagus with dysplasia"),
        ],
        "procedures": [
            Procedure(
                name="Upper endoscopy with biopsy",
                code=None,
                indication="Diagnostic confirmation and surveillance",
            ),
            Procedure(
                name="Endoscopic eradication therapy",
                code=None,
                indication="Selected patients with dysplasia or early neoplasia",
            ),
            Procedure(
                name="Esophagectomy",
                code=None,
                indication="Rare selected cases with advanced disease or cancer",
            ),
        ],
        "treatments": [
            Treatment(
                name="Acid suppression therapy",
                type="Pharmacological",
                line="GERD management",
                notes="Used to control reflux symptoms and esophagitis.",
            ),
            Treatment(
                name="Endoscopic surveillance",
                type="Procedural / monitoring",
                line="Ongoing management",
                notes="Used according to dysplasia status and risk profile.",
            ),
            Treatment(
                name="Endoscopic eradication therapy",
                type="Procedural",
                line="Dysplasia or selected high-risk disease",
                notes="Used in selected patients.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NIDDK Barrett's Esophagus",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/barretts-esophagus",
                accessed="2026-04-29",
            ),
            Source(
                name="NIDDK Barrett's Esophagus Diagnosis",
                url="https://www.niddk.nih.gov/health-information/digestive-diseases/barretts-esophagus/diagnosis",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "Dysplasia status is important but may be incompletely captured without pathology data.",
            "Endoscopic surveillance intervals and biopsy findings are usually not visible in claims data.",
            "Distinguishing Barrett's esophagus from GERD alone requires endoscopy, pathology, or specific diagnosis coding.",
        ],
    },
    "hepatocellular carcinoma": {
        "normalized_term": "Hepatocellular Carcinoma",
        "aliases": [
            "hcc",
            "hepatocellular carcinoma",
            "liver cancer",
            "primary liver cancer",
        ],
        "overview": (
            "Hepatocellular carcinoma is the most common type of primary liver cancer and often occurs in the setting of chronic liver disease or cirrhosis. "
            "Management depends on tumor burden, liver function, performance status, and transplant eligibility."
        ),
        "symptoms": [
            "Often asymptomatic in early disease",
            "Right upper abdominal pain or fullness",
            "Unexplained weight loss",
            "Jaundice or worsening liver function",
            "Ascites or signs of advanced liver disease",
        ],
        "diagnosis": [
            "Liver imaging such as multiphasic CT or MRI",
            "Assessment of underlying liver disease and cirrhosis status",
            "Alpha-fetoprotein testing as a supportive marker in selected patients",
            "Biopsy in selected cases when imaging is indeterminate",
        ],
        "icd_codes": [
            ICDCode(code="C22.0", description="Liver cell carcinoma"),
        ],
        "procedures": [
            Procedure(
                name="Multiphasic liver CT or MRI",
                code=None,
                indication="Diagnosis, staging, and treatment planning",
            ),
            Procedure(
                name="Tumor ablation", code=None, indication="Selected localized tumors"
            ),
            Procedure(
                name="Transarterial therapy",
                code=None,
                indication="Selected intermediate-stage or unresectable disease",
            ),
            Procedure(
                name="Liver transplant evaluation",
                code=None,
                indication="Selected candidates with tumor and liver disease criteria",
            ),
        ],
        "treatments": [
            Treatment(
                name="Surgical resection",
                type="Procedural / surgical",
                line="Selected localized disease",
                notes="Used in selected patients with adequate liver function.",
            ),
            Treatment(
                name="Liver transplant",
                type="Procedural / transplant",
                line="Selected eligible patients",
                notes="Considered when tumor burden and liver disease criteria are met.",
            ),
            Treatment(
                name="Locoregional therapy",
                type="Procedural / interventional",
                line="Selected localized or intermediate disease",
                notes="Includes ablation and embolization-based approaches.",
            ),
            Treatment(
                name="Systemic therapy",
                type="Pharmacological / biologic",
                line="Advanced disease",
                notes="Includes targeted therapy or immunotherapy depending on disease setting and patient factors.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="NCI Liver Cancer Treatment",
                url="https://www.cancer.gov/types/liver/what-is-liver-cancer/treatment",
                accessed="2026-04-29",
            ),
            Source(
                name="NCI Primary Liver Cancer Treatment PDQ",
                url="https://www.cancer.gov/types/liver/hp/adult-liver-treatment-pdq",
                accessed="2026-04-29",
            ),
        ],
        "data_considerations": [
            "HCC analysis requires integration of cancer diagnosis, liver disease severity, imaging, locoregional procedures, and systemic therapy.",
            "Tumor stage, liver function scores, and transplant criteria are often incomplete in claims data.",
            "Underlying cirrhosis, viral hepatitis, MASLD/MASH, alcohol-related liver disease, and surveillance history may be important stratifiers.",
        ],
    },
}
