from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_clinical_intel_lookup() -> None:
    response = client.post('/api/clinical-intel', json={'query': 'iTTP'})
    assert response.status_code == 200
    body = response.json()
    assert body['normalized_term'] == 'Immune Thrombotic Thrombocytopenic Purpura'
    assert len(body['icd_codes']) >= 1
