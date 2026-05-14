from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_GI = {
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
        "diagnostic_considerations": [
            "Crohn’s disease diagnosis usually requires integration of symptoms, endoscopy, histology, imaging, and exclusion of infectious or alternative inflammatory causes.",
            "Disease location and behavior should be characterized where possible, including ileal, colonic, ileocolonic, stricturing, penetrating, and perianal disease patterns.",
            "Cross-sectional imaging such as MR enterography or CT enterography may be important when small bowel disease, strictures, fistulas, or abscesses are suspected.",
            "Fecal calprotectin and inflammatory markers may support assessment of intestinal inflammation but are not diagnostic alone.",
            "In real-world data, Crohn’s disease may be confused with ulcerative colitis or nonspecific colitis unless longitudinal diagnosis, procedure, pathology, and treatment patterns are considered.",
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
        "diagnostic_considerations": [
            "Ulcerative colitis diagnosis generally requires integration of clinical symptoms, endoscopic findings, histology, and exclusion of infectious colitis or alternative inflammatory conditions.",
            "Disease extent should be characterized where possible, including proctitis, left-sided colitis, or extensive pancolitis involvement.",
            "Endoscopic assessment is important for evaluating disease severity, mucosal inflammation, and treatment response.",
            "Inflammatory markers and fecal calprotectin may support assessment of inflammatory activity but are not diagnostic independently.",
            "In real-world data, ulcerative colitis may be difficult to distinguish from Crohn’s disease, indeterminate colitis, or nonspecific colitis without longitudinal clinical and procedural context.",
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
}
