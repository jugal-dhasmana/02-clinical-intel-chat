\# ClinicalIntelChat Deployment Runbook



\## Project



ClinicalIntelChat



Clinical intelligence platform focused on therapy level insights across GI and rare diseases.



Initial therapies:



\* iTTP

\* Crohn's Disease

\* Ulcerative Colitis

\* Hemophilia A

\* Short Bowel Syndrome



Core stack:



\* FastAPI

\* Python

\* Pydantic

\* Real World Data principles

\* Therapy normalization logic



\---



\# Phase 1. Repository Hygiene



\## 1. Confirm Git Installation



Run:



```bash

git --version

```



Expected:



```text

git version x.xx.x

```



Status:



\* Completed



\---



\## 2. Confirm Git Repository Status



Run:



```bash

git status

```



Expected:



```text

On branch main

Your branch is up to date with 'origin/main'.



nothing to commit, working tree clean

```



Status:



\* Completed

\* Branch: main

\* Remote connected: Yes



\---



\## 3. Inspect Repository Structure



Current top-level structure:



```text

02-clinical-intel-chat/

│

├── .git/

├── .gitignore

├── LICENSE

├── backend/

├── frontend/

├── docs/

├── data/

├── ProjectPlan/

└── README.md

```



Status:



\* Good structure for early-stage application



\---



\## 4. Check for Environment Files



Run:



```bash

dir /s /b \*.env

```



Expected:



```text

File Not Found

```



Actual Result:



\* No `.env` files found



Status:



\* Safe



\---



\## 5. Check for Secrets, Keys, Tokens



Run:



```bash

dir /s /b \*secret\*

dir /s /b \*key\*

dir /s /b \*token\*

```



Observed Results:



\* Only package/library related files inside Python virtual environment

\* No project secrets detected



Example safe paths:



```text

backend\\venv\\Lib\\site-packages\\

```



Status:



\* Safe



\---



\## 6. Confirm Virtual Environment is NOT Tracked by Git



Run:



```bash

git ls-files backend/venv

```



Expected:



\* No output



Actual Result:



\* No output



Status:



\* Correctly excluded from Git



\---



\## 7. Validate `.gitignore`



Run:



```bash

findstr /i "venv .env \_\_pycache\_\_" .gitignore

```



Confirmed protections:



```text

.env

.envrc

.venv

venv/

venv.bak/

\_\_pycache\_\_/

```



Status:



\* Properly configured



\---



\# Repository Hygiene Assessment



\## Current Health Status



| Area                    | Status |

| ----------------------- | ------ |

| Git initialized         | PASS   |

| GitHub connected        | PASS   |

| Branch clean            | PASS   |

| Sensitive `.env` files  | PASS   |

| Secrets detected        | PASS   |

| `venv` tracked by Git   | PASS   |

| `.gitignore` protection | PASS   |

| README present          | PASS   |

| LICENSE present         | PASS   |



Overall Assessment:



\* Repository is clean and suitable for deployment preparation.



\---



\# Upcoming Deployment Phases



\## Phase 2. Deployment Architecture Decision



Evaluate hosting platform options:



Potential platforms:



\* Render

\* Railway

\* Fly.io

\* Azure

\* AWS

\* Google Cloud

\* DigitalOcean



Decision factors:



\* Beginner friendliness

\* FastAPI compatibility

\* Free tier stability

\* Scalability

\* Simplicity

\* Cost management

\* Future production readiness



\---



\## Phase 3. Backend Production Preparation



Planned tasks:



\* requirements.txt validation

\* environment variable setup

\* startup command standardization

\* production logging

\* CORS configuration

\* health check endpoint

\* API documentation cleanup



\---



\## Phase 4. Public Deployment



Planned tasks:



\* public hosting

\* HTTPS

\* public API URL

\* Swagger exposure

\* uptime validation



\---



\## Phase 5. Open Source Readiness



Planned tasks:



\* contributor strategy

\* licensing review

\* README enhancement

\* screenshots

\* architecture diagrams

\* roadmap

\* issue templates



\---



\# Notes



Important principles learned:



\* Never commit `.env` files

\* Never track `venv`

\* Always verify `.gitignore`

\* Keep deployment concerns separate from application development

\* Small polished therapy coverage is stronger than large unstable coverage



\---



\# Current Project Position



ClinicalIntelChat is currently in:



\* Functional prototype stage

\* Early deployment preparation stage

\* Public release planning stage



The repository hygiene foundation is strong for a first application project.


## Phase 2. Local Backend Validation

### 1. Start backend locally

From project root:

```bash
cd backend
python -m uvicorn app.main:app --reload



Uvicorn running on http://127.0.0.1:8000
Application startup complete.
