from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_LIVER = {
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
            "Nonalcoholic steatohepatitis, now commonly referred to as metabolic dysfunction-associated steatohepatitis, is a progressive form of fatty liver disease characterized by hepatic fat accumulation with inflammation and liver cell injury. "
            "It may progress to fibrosis, cirrhosis, liver failure, or hepatocellular carcinoma in selected patients.\n\n"
            "Global / U.S. Epidemiology: MASH/NASH is part of the broader MASLD/NAFLD spectrum. U.S. estimates suggest about 24% of adults have NAFLD and about 1.5% to 6.5% have NASH/MASH."
        ),
        "causes": [
            "Metabolic dysfunction leading to hepatic fat accumulation, inflammation, and liver cell injury.",
            "Often associated with insulin resistance, obesity, type 2 diabetes, dyslipidemia, and cardiometabolic risk.",
        ],
        "risk_factors": [
            "Obesity or central adiposity",
            "Type 2 diabetes",
            "Insulin resistance or metabolic syndrome",
            "Dyslipidemia",
            "Hypertension or other cardiometabolic risk factors",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis requires assessment of hepatic steatosis, inflammation, fibrosis risk, and exclusion of other liver diseases.",
            "Liver biopsy remains the reference standard for confirming steatohepatitis and fibrosis stage, but noninvasive fibrosis assessment is commonly used in practice.",
            "Noninvasive tools may include liver enzymes, FIB-4, elastography, imaging, and serum-based fibrosis markers.",
            "Patients with type 2 diabetes, obesity, or metabolic syndrome may warrant higher suspicion for advanced fibrosis.",
            "In real-world data, fibrosis stage, histology, imaging results, alcohol exposure, and metabolic risk details may be incompletely captured.",
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
    "primary biliary cholangitis": {
        "normalized_term": "Primary Biliary Cholangitis",
        "aliases": [
            "primary biliary cholangitis",
            "pbc",
            "primary biliary cirrhosis",
        ],
        "overview": (
            "Primary biliary cholangitis is a chronic autoimmune cholestatic liver disease in which small intrahepatic bile ducts become injured and inflamed, leading to bile retention and potential progressive liver damage.\n\n"
            "Global / U.S. Epidemiology: PBC is a rare disease with pooled global prevalence estimated around 14.6 to 18.1 cases per 100,000 people, with higher reported prevalence in some North American and European populations."
        ),
        "causes": [
            "Autoimmune injury targeting small intrahepatic bile ducts.",
            "Progressive bile duct destruction can lead to cholestasis, fibrosis, cirrhosis, and liver failure in some patients.",
        ],
        "risk_factors": [
            "Female sex",
            "Middle age or older age",
            "Family history of primary biliary cholangitis",
            "Personal or family history of autoimmune disease",
            "Environmental and genetic susceptibility factors",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is commonly supported by cholestatic liver enzyme elevation and antimitochondrial antibody positivity.",
            "Imaging is often used to exclude extrahepatic biliary obstruction or alternative cholestatic liver disease.",
            "Liver biopsy may be useful when diagnosis is uncertain or overlap with autoimmune hepatitis is suspected.",
            "Biochemical response to therapy is important for prognosis and treatment escalation decisions.",
            "In real-world data, autoantibody status, alkaline phosphatase trends, fibrosis stage, symptoms, and treatment response may require linked labs or EMR data.",
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
            "It is often associated with inflammatory bowel disease and may progress to cirrhosis, biliary complications, liver transplant need, or hepatobiliary malignancy.\n\n"
            "Global / U.S. Epidemiology: PSC is rare, with prevalence estimates varying widely by geography. Pooled global estimates are commonly around 11 to 14 cases per 100,000 people, with higher rates reported in some Northern European and North American populations."
        ),
        "causes": [
            "Chronic inflammatory and fibrosing injury of intrahepatic and/or extrahepatic bile ducts.",
            "Exact cause is not fully understood, but immune-mediated, genetic, microbiome, and inflammatory bowel disease-related mechanisms are implicated.",
        ],
        "risk_factors": [
            "Inflammatory bowel disease, especially ulcerative colitis",
            "Male sex",
            "Younger to middle adult age at diagnosis",
            "Family history of primary sclerosing cholangitis or inflammatory bowel disease",
            "Northern European ancestry or residence in higher-prevalence regions",
        ],
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
        "diagnostic_considerations": [
            "Diagnosis is commonly supported by cholestatic liver enzyme abnormalities and characteristic bile duct changes on MRCP or ERCP.",
            "Secondary causes of sclerosing cholangitis should be excluded where clinically appropriate.",
            "Associated inflammatory bowel disease should be assessed because it affects surveillance and longitudinal management.",
            "Dominant strictures, cholangitis, cirrhosis, transplant evaluation, and cholangiocarcinoma risk are important clinical considerations.",
            "In real-world data, bile duct imaging findings, liver biochemistry trends, IBD phenotype, malignancy surveillance, and transplant status may be incompletely captured.",
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
}
