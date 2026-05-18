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
            "Crohn's disease is a chronic inflammatory bowel disease characterized by transmural inflammation that can affect any part of the gastrointestinal tract, most commonly the terminal ileum and colon. "
            "It often follows a relapsing and remitting course and may lead to complications such as strictures, fistulas, abscesses, and nutritional deficiencies.\n\n"
            "Global / U.S. Epidemiology: Crohn's disease prevalence varies by geography and is highest in North America and Europe. Recent global estimates report Crohn's disease prevalence around 84 per 100,000 people, while U.S. estimates suggest approximately 1 million people are living with Crohn's disease."
        ),
        "causes": [
            "Chronic immune-mediated inflammation involving the gastrointestinal tract.",
            "Likely multifactorial pathogenesis involving genetic susceptibility, intestinal microbiome changes, environmental exposures, and dysregulated immune response.",
        ],
        "risk_factors": [
            "Family history of inflammatory bowel disease",
            "Cigarette smoking",
            "Younger adult age at onset, commonly between ages 20 and 29",
            "Ashkenazi Jewish ancestry",
            "Residence in industrialized regions or environments associated with higher IBD prevalence",
        ],
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
            "Ulcerative colitis is a chronic inflammatory bowel disease characterized by continuous mucosal inflammation of the colon, beginning in the rectum and extending proximally to varying degrees. "
            "Patients commonly experience relapsing and remitting symptoms including diarrhea, rectal bleeding, abdominal pain, and urgency.\n\n"
            "Global / U.S. Epidemiology: Ulcerative colitis prevalence is highest in North America and Europe. Global prevalence estimates are commonly reported around 87 per 100,000 people, while U.S. estimates suggest approximately 600,000 to 900,000 individuals are living with ulcerative colitis."
        ),
        "causes": [
            "Chronic immune-mediated inflammation involving the colonic mucosa.",
            "Likely multifactorial pathogenesis involving genetic susceptibility, altered gut microbiome, environmental exposures, and dysregulated immune response.",
        ],
        "risk_factors": [
            "Family history of inflammatory bowel disease",
            "Younger age at disease onset, often between ages 15 and 30",
            "Ashkenazi Jewish ancestry",
            "Residence in industrialized regions with higher inflammatory bowel disease prevalence",
            "Certain environmental and microbiome-related exposures associated with immune dysregulation",
        ],
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
            "Celiac disease is a chronic immune-mediated digestive disorder triggered by gluten exposure in genetically susceptible individuals. "
            "It damages the small intestine and may cause gastrointestinal symptoms, nutrient deficiencies, and extraintestinal manifestations.\n\n"
            "Global / U.S. Epidemiology: Celiac disease affects populations worldwide with estimated global prevalence around 1% of the population. "
            "U.S. prevalence is also estimated near 1%, although many individuals remain undiagnosed or are diagnosed after prolonged symptoms."
        ),
        "causes": [
            "Immune-mediated reaction to gluten exposure in genetically susceptible individuals.",
            "Gluten ingestion triggers inflammatory injury and villous atrophy in the small intestine.",
        ],
        "risk_factors": [
            "Family history of celiac disease",
            "Type 1 diabetes or other autoimmune disorders",
            "Genetic predisposition including HLA-DQ2 or HLA-DQ8 positivity",
            "First-degree relatives with celiac disease",
            "Autoimmune thyroid disease or Down syndrome",
        ],
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
        "diagnostic_considerations": [
            "Accurate serologic testing generally requires active gluten consumption before testing.",
            "Small bowel biopsy remains important in many adult patients for diagnostic confirmation and assessment of villous atrophy.",
            "Differential diagnosis may include irritable bowel syndrome, inflammatory bowel disease, lactose intolerance, small intestinal bacterial overgrowth, and non-celiac gluten sensitivity.",
            "Associated autoimmune diseases and nutritional deficiencies should be evaluated where clinically appropriate.",
            "In real-world data, diagnosis confirmation may be challenging because biopsy results, serology, dietary adherence, and symptom response are often incompletely captured.",
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
            "Eosinophilic esophagitis is a chronic immune-mediated inflammatory disease of the esophagus characterized by eosinophil-predominant inflammation and symptoms of esophageal dysfunction.\n\n"
            "Global / U.S. Epidemiology: Eosinophilic esophagitis prevalence has increased substantially over recent decades. "
            "Current prevalence estimates are commonly reported around 30 to 60 cases per 100,000 people in the United States and other developed regions."
        ),
        "causes": [
            "Chronic immune-mediated inflammatory response involving the esophagus.",
            "Food and environmental antigen exposure are believed to contribute to eosinophilic inflammation in genetically susceptible individuals.",
        ],
        "risk_factors": [
            "Male sex",
            "Personal or family history of atopic disease",
            "Asthma, eczema, allergic rhinitis, or food allergies",
            "Younger age at diagnosis",
            "Family history of eosinophilic esophagitis",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis requires symptoms of esophageal dysfunction together with eosinophil-predominant inflammation on esophageal biopsy.",
            "Alternative causes of esophageal eosinophilia including gastroesophageal reflux disease and infections should be considered.",
            "Endoscopic findings may include rings, furrows, edema, strictures, or white exudates, although appearance can vary.",
            "Disease monitoring often requires repeat endoscopy and biopsy assessment.",
            "In real-world data, definitive diagnosis may be difficult because pathology and endoscopic findings are often unavailable in claims-only datasets.",
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
            "It can cause chronic upper gastrointestinal symptoms and may be associated with diabetes, postsurgical states, medications, neurologic disease, or idiopathic causes.\n\n"
            "Global / U.S. Epidemiology: Gastroparesis is an uncommon but clinically significant gastrointestinal motility disorder. "
            "U.S. prevalence estimates vary by population and methodology but are commonly reported between approximately 10 and 40 cases per 100,000 people, with higher prevalence among women and individuals with diabetes."
        ),
        "causes": [
            "Delayed gastric emptying due to impaired gastric motility or abnormal neuromuscular regulation.",
            "Associated causes may include diabetes, postsurgical vagal nerve injury, neurologic disease, medications, or idiopathic dysfunction.",
        ],
        "risk_factors": [
            "Diabetes mellitus",
            "Female sex",
            "Prior upper gastrointestinal surgery",
            "Neurologic disorders affecting autonomic function",
            "Use of medications that slow gastric emptying such as opioids or GLP-1 related therapies",
        ],
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
        "diagnostic_considerations": [
            "Mechanical obstruction should be excluded before establishing a diagnosis of gastroparesis.",
            "Objective evidence of delayed gastric emptying is important for diagnostic confirmation.",
            "Symptoms may overlap with functional dyspepsia, medication effects, cyclic vomiting syndrome, and other upper gastrointestinal disorders.",
            "Diabetic gastroparesis should be evaluated in the context of glycemic control and autonomic dysfunction.",
            "In real-world data, gastric emptying study results and symptom severity are often unavailable, limiting diagnostic specificity.",
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
            "Chronic pancreatitis is a long-standing inflammatory disease of the pancreas that can lead to irreversible structural damage, chronic abdominal pain, exocrine pancreatic insufficiency, diabetes, and nutritional complications.\n\n"
            "Global / U.S. Epidemiology: Chronic pancreatitis is an uncommon but clinically significant pancreatic disorder. "
            "Reported prevalence estimates commonly range from approximately 30 to 50 cases per 100,000 people globally, with higher rates in populations with significant alcohol and smoking exposure."
        ),
        "causes": [
            "Chronic pancreatic inflammation resulting in irreversible structural and functional pancreatic damage.",
            "Common etiologies include alcohol exposure, genetic factors, obstructive disease, autoimmune pancreatitis, and recurrent acute pancreatitis.",
        ],
        "risk_factors": [
            "Heavy alcohol use",
            "Cigarette smoking",
            "Recurrent acute pancreatitis",
            "Genetic predisposition including PRSS1, SPINK1, or CFTR mutations",
            "Obstructive pancreatic duct disease or autoimmune pancreatitis",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis often requires integration of clinical symptoms, imaging findings, pancreatic function assessment, and longitudinal disease history.",
            "Differential diagnosis may include pancreatic cancer, recurrent acute pancreatitis, biliary disease, and other chronic abdominal pain syndromes.",
            "Exocrine pancreatic insufficiency and diabetes should be evaluated in advanced disease.",
            "Alcohol and smoking exposure are important contributors to disease progression and complications.",
            "In real-world data, imaging detail, alcohol exposure, smoking status, and pancreatic function testing are often incompletely captured.",
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
