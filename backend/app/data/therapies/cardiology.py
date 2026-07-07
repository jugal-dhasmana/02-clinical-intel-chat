from app.schemas.clinical_intel import ICDCode, Procedure, Treatment, Source

THERAPIES_CARDIOLOGY = {
    "heart failure": {
        "normalized_term": "Heart Failure / Congestive Heart Failure",
        "aliases": [
            "heart failure",
            "congestive heart failure",
            "chf",
            "hf",
            "hfrEF",
            "hfpef",
            "hfmref",
            "systolic heart failure",
            "diastolic heart failure",
            "right heart failure",
            "acute decompensated heart failure",
            "advanced heart failure",
        ],
        "overview": (
            "Heart failure is a chronic clinical syndrome in which the heart is unable to pump or fill effectively enough to meet the body's needs. "
            "It may result from structural or functional cardiac disease and can present with congestion, reduced exercise tolerance, fluid retention, and recurrent hospitalization risk.\n\n"
            "Global / U.S. Epidemiology: Heart failure is common and increases with age. In the United States, approximately 6.7 million adults are estimated to have heart failure, and prevalence is expected to rise as the population ages."
        ),
        "causes": [
            "Reduced or impaired cardiac pumping, filling, or relaxation due to structural or functional heart disease.",
            "Common causes include coronary artery disease, myocardial infarction, hypertension, valvular heart disease, cardiomyopathy, arrhythmias, diabetes-related cardiac disease, and chronic kidney disease.",
        ],
        "risk_factors": [
            "Older age",
            "Hypertension",
            "Coronary artery disease or prior myocardial infarction",
            "Diabetes mellitus",
            "Obesity, chronic kidney disease, atrial fibrillation, and valvular heart disease",
        ],
        "symptoms": [
            "Shortness of breath with exertion or at rest",
            "Fatigue or reduced exercise tolerance",
            "Peripheral edema or fluid retention",
            "Orthopnea or paroxysmal nocturnal dyspnea",
            "Rapid weight gain or abdominal swelling from congestion",
        ],
        "diagnosis": [
            "Clinical evaluation of symptoms, signs of congestion, medical history, and cardiovascular risk factors",
            "Echocardiography to assess ejection fraction, structure, valve disease, and cardiac function",
            "BNP or NT-proBNP testing as supportive evidence when heart failure is suspected",
            "Electrocardiogram, chest imaging, laboratory testing, and evaluation for ischemic or structural heart disease",
        ],
        "diagnostic_considerations": [
            "Heart failure should be characterized by ejection fraction phenotype when possible: HFrEF, HFmrEF, HFpEF, or heart failure with improved ejection fraction.",
            "HFrEF generally refers to heart failure with reduced ejection fraction, commonly LVEF 40% or lower.",
            "HFmrEF refers to mildly reduced ejection fraction, commonly LVEF 41% to 49%.",
            "HFpEF refers to preserved ejection fraction, commonly LVEF 50% or higher, usually requiring objective evidence of cardiac dysfunction or congestion.",
            "Acute decompensated heart failure, right-sided heart failure, and advanced heart failure should be distinguished when clinically relevant because treatment pathways and outcomes differ.",
            "In real-world data, ejection fraction, NYHA class, natriuretic peptide values, volume status, and symptom burden are often incompletely captured.",
        ],
        "icd_codes": [
            ICDCode(code="I50.9", description="Heart failure, unspecified"),
            ICDCode(code="I50.20", description="Unspecified systolic heart failure"),
            ICDCode(code="I50.21", description="Acute systolic heart failure"),
            ICDCode(code="I50.22", description="Chronic systolic heart failure"),
            ICDCode(code="I50.23", description="Acute on chronic systolic heart failure"),
            ICDCode(code="I50.30", description="Unspecified diastolic heart failure"),
            ICDCode(code="I50.31", description="Acute diastolic heart failure"),
            ICDCode(code="I50.32", description="Chronic diastolic heart failure"),
            ICDCode(code="I50.33", description="Acute on chronic diastolic heart failure"),
            ICDCode(code="I50.40", description="Unspecified combined systolic and diastolic heart failure"),
            ICDCode(code="I50.41", description="Acute combined systolic and diastolic heart failure"),
            ICDCode(code="I50.42", description="Chronic combined systolic and diastolic heart failure"),
            ICDCode(code="I50.43", description="Acute on chronic combined systolic and diastolic heart failure"),
            ICDCode(code="I50.810", description="Right heart failure, unspecified"),
            ICDCode(code="I50.811", description="Acute right heart failure"),
            ICDCode(code="I50.812", description="Chronic right heart failure"),
            ICDCode(code="I50.813", description="Acute on chronic right heart failure"),
        ],
        "procedures": [
            Procedure(
                name="Echocardiography",
                code=None,
                indication="Assess ejection fraction, cardiac structure, valve disease, and functional phenotype",
            ),
            Procedure(
                name="BNP or NT-proBNP testing",
                code=None,
                indication="Support diagnosis and risk stratification in suspected or established heart failure",
            ),
            Procedure(
                name="Cardiac catheterization or coronary evaluation",
                code=None,
                indication="Evaluate ischemic heart disease when clinically appropriate",
            ),
            Procedure(
                name="Implantable cardioverter-defibrillator or cardiac resynchronization therapy evaluation",
                code=None,
                indication="Selected patients with reduced ejection fraction and guideline-based eligibility",
            ),
        ],
        "treatments": [
            Treatment(
                name="Guideline-directed medical therapy for HFrEF",
                type="Pharmacological",
                line="Foundational HFrEF management",
                notes="Often includes ARNI or ACE inhibitor or ARB, beta blocker, mineralocorticoid receptor antagonist, and SGLT2 inhibitor when appropriate.",
            ),
            Treatment(
                name="Diuretics",
                type="Pharmacological",
                line="Congestion management",
                notes="Used to manage volume overload and symptoms of congestion across heart failure phenotypes.",
            ),
            Treatment(
                name="SGLT2 inhibitor therapy",
                type="Pharmacological",
                line="Selected HF phenotypes",
                notes="Used in HFrEF and selected HFmrEF/HFpEF patients according to clinical criteria and guidelines.",
            ),
            Treatment(
                name="Device therapy",
                type="Procedural / device",
                line="Selected HFrEF patients",
                notes="ICD or CRT may be considered in selected patients based on ejection fraction, rhythm, QRS duration, symptoms, and prognosis.",
            ),
            Treatment(
                name="Advanced heart failure therapies",
                type="Procedural / advanced care",
                line="Advanced disease",
                notes="May include transplant evaluation, left ventricular assist device, palliative care, or specialty heart failure management in selected patients.",
            ),
        ],
        "clinical_trials": [],
        "literature": [],
        "sources": [
            Source(
                name="CDC Heart Failure",
                url="https://www.cdc.gov/heart-disease/about/heart-failure.html",
                accessed="2026-07-07",
            ),
            Source(
                name="2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure",
                url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000001063",
                accessed="2026-07-07",
            ),
            Source(
                name="ICD-10-CM I50 Heart Failure Codes",
                url="https://www.icd10data.com/ICD10CM/Codes/I00-I99/I30-I5A/I50-",
                accessed="2026-07-07",
            ),
        ],
        "data_considerations": [
            "Claims data can identify heart failure diagnoses, hospitalizations, procedures, and medication exposure, but usually lacks ejection fraction and NYHA class.",
            "HFrEF, HFmrEF, and HFpEF classification often requires linked echocardiography, structured EMR fields, or clinical notes.",
            "Acute decompensated heart failure may be inferred from inpatient or emergency encounters with heart failure diagnosis plus diuretic, oxygen, ICU, or discharge patterns.",
            "Medication exposure should combine pharmacy and medical claims where applicable, especially for injected or administered therapies and device-related care.",
            "Comorbidities such as CKD, diabetes, atrial fibrillation, obesity, COPD, coronary artery disease, and hypertension are important for risk adjustment and cohort interpretation.",
        ],
    },
}