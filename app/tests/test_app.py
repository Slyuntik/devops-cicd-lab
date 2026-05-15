import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.json['service'] == 'devops-cicd-demo'

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.json['status'] == 'ok'

def test_greeting_without_feature_flag(client):
    rv = client.get('/greeting')
    assert rv.json['message'] == 'Hello, world!'

def test_greeting_with_feature_flag(client, monkeypatch):
    monkeypatch.setenv('FEATURE_NEW_GREETING', 'true')
    rv = client.get('/greeting')
    assert rv.json['message'] == 'Hello from new feature!'