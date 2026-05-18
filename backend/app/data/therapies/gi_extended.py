from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_GI_ONCOLOGY = {
    "irritable bowel syndrome": {
        "normalized_term": "Irritable Bowel Syndrome",
        "aliases": ["ibs", "irritable bowel syndrome", "spastic colon"],
        "overview": (
            "Irritable bowel syndrome is a chronic disorder of gut-brain interaction characterized by recurrent abdominal pain associated with altered bowel habits, including diarrhea, constipation, or mixed patterns.\n\n"
            "Global / U.S. Epidemiology: IBS is common worldwide. Studies suggest approximately 12% of people in the United States have IBS, with higher reported frequency among women and people younger than age 50."
        ),
        "causes": [
            "Disordered gut-brain interaction affecting intestinal sensitivity, motility, and symptom perception.",
            "Symptoms may be influenced by visceral hypersensitivity, altered motility, microbiome changes, prior infection, stress, and dietary triggers.",
        ],
        "risk_factors": [
            "Female sex",
            "Age younger than 50",
            "Family history of IBS",
            "History of stressful or traumatic life events",
            "Prior gastrointestinal infection",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is symptom-based and often uses Rome criteria in clinical or research settings.",
            "Alarm features such as gastrointestinal bleeding, unexplained weight loss, anemia, fever, or nocturnal symptoms should prompt evaluation for alternative diagnoses.",
            "IBS subtype should be characterized by predominant bowel habit, including IBS-D, IBS-C, IBS-M, or unclassified IBS.",
            "Differential diagnosis may include inflammatory bowel disease, celiac disease, colorectal cancer, infection, microscopic colitis, and medication effects.",
            "In real-world data, IBS subtype, symptom frequency, alarm features, and diagnostic exclusion workup are often incompletely captured.",
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
            "Exocrine pancreatic insufficiency is a condition in which inadequate pancreatic enzyme activity leads to impaired digestion and malabsorption, often associated with chronic pancreatitis, pancreatic surgery, cystic fibrosis, or pancreatic cancer.\n\n"
            "Global / U.S. Epidemiology: EPI prevalence in the general population is not well established because it is commonly tied to underlying pancreatic or systemic diseases. It is most often recognized in patients with chronic pancreatitis, cystic fibrosis, pancreatic cancer, pancreatic surgery, or other high-risk conditions."
        ),
        "causes": [
            "Insufficient delivery or activity of pancreatic digestive enzymes in the intestine.",
            "Common underlying causes include chronic pancreatitis, cystic fibrosis, pancreatic cancer, pancreatic surgery, and other pancreatic or gastrointestinal disorders.",
        ],
        "risk_factors": [
            "Chronic pancreatitis",
            "Cystic fibrosis",
            "Pancreatic cancer or pancreatic surgery",
            "History of heavy alcohol use or smoking through chronic pancreatitis pathway",
            "Longstanding diabetes or other pancreatic disease in selected patients",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is supported by symptoms of malabsorption, risk factors, and pancreatic function testing such as fecal elastase when available.",
            "Symptoms may overlap with celiac disease, inflammatory bowel disease, small intestinal bacterial overgrowth, bile acid diarrhea, and functional gastrointestinal disorders.",
            "Underlying etiology should be identified because prognosis and management differ by cause.",
            "Nutritional deficiencies and fat-soluble vitamin status may require assessment in clinically significant disease.",
            "In real-world data, fecal elastase values, stool fat testing, nutrition status, and severity of malabsorption are often unavailable.",
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
            "Gastroesophageal reflux disease is a chronic condition in which stomach contents reflux into the esophagus and cause bothersome symptoms or complications such as esophagitis, stricture, or Barrett's esophagus.\n\n"
            "Global / U.S. Epidemiology: GERD is common in the United States. Researchers estimate that about 20% of people in the United States have GERD."
        ),
        "causes": [
            "Reflux of gastric contents into the esophagus due to impaired antireflux barrier function or abnormal esophageal clearance.",
            "Contributing mechanisms may include lower esophageal sphincter dysfunction, hiatal hernia, delayed gastric emptying, obesity-related pressure effects, or medication effects.",
        ],
        "risk_factors": [
            "Overweight or obesity",
            "Pregnancy",
            "Smoking or secondhand smoke exposure",
            "Hiatal hernia",
            "Use of medications that may worsen reflux in selected patients",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is often clinical in patients with typical heartburn and regurgitation symptoms.",
            "Upper endoscopy is important when alarm symptoms, dysphagia, bleeding, weight loss, anemia, or complications are suspected.",
            "Ambulatory reflux monitoring may be used in uncertain, refractory, or pre-procedural cases.",
            "Differential diagnosis may include eosinophilic esophagitis, functional heartburn, cardiac chest pain, peptic ulcer disease, and motility disorders.",
            "In real-world data, over-the-counter medication use, symptom burden, endoscopic severity, and reflux monitoring results are often incompletely captured.",
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
            "It is clinically important because it is associated with increased risk of esophageal adenocarcinoma.\n\n"
            "Global / U.S. Epidemiology: Barrett's esophagus prevalence is uncertain, but population estimates are commonly reported around 1% to 2%, with higher prevalence among patients with chronic GERD."
        ),
        "causes": [
            "Metaplastic change of the distal esophageal lining, commonly associated with chronic gastroesophageal reflux exposure.",
            "Chronic acid and bile reflux may contribute to intestinal metaplasia and dysplasia risk in susceptible individuals.",
        ],
        "risk_factors": [
            "Chronic GERD",
            "Male sex",
            "Age over 50",
            "White race",
            "Obesity or central adiposity",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis requires endoscopic identification of suspected Barrett's mucosa with biopsy confirmation when clinically appropriate.",
            "Dysplasia status is central to surveillance intervals and treatment planning.",
            "Differential diagnosis may include irregular Z-line, esophagitis, gastric intestinal metaplasia, and esophageal adenocarcinoma.",
            "Patients with chronic GERD and multiple risk factors may be considered for screening based on clinical guidance.",
            "In real-world data, pathology confirmation, segment length, dysplasia grade, and surveillance intervals are often incompletely captured.",
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
            "Management depends on tumor burden, liver function, performance status, and transplant eligibility.\n\n"
            "Global / U.S. Epidemiology: HCC is a major global cancer burden and occurs most often in patients with chronic liver disease. In the United States, liver and intrahepatic bile duct cancer incidence is approximately 9.5 new cases per 100,000 people per year."
        ),
        "causes": [
            "Malignant transformation of hepatocytes, most commonly in the setting of chronic liver injury, fibrosis, or cirrhosis.",
            "Common underlying drivers include chronic hepatitis B, chronic hepatitis C, alcohol-related liver disease, MASLD/MASH, and cirrhosis from other causes.",
        ],
        "risk_factors": [
            "Cirrhosis from any cause",
            "Chronic hepatitis B infection",
            "Chronic hepatitis C infection",
            "Alcohol-related liver disease",
            "MASLD/MASH and metabolic risk factors such as obesity or diabetes",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis often relies on characteristic imaging findings on multiphasic CT or MRI in at-risk patients.",
            "Tumor burden, liver function, portal hypertension, performance status, and transplant eligibility are central to treatment selection.",
            "Alpha-fetoprotein may support surveillance or evaluation but is not diagnostic alone.",
            "Differential diagnosis may include cholangiocarcinoma, metastatic liver disease, benign liver lesions, and mixed tumors.",
            "In real-world data, tumor stage, imaging criteria, liver function scores, transplant eligibility, and treatment intent are often incompletely captured.",
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
