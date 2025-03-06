import pytest
from app import app

@pytest.fixture
def client():
    """Creates a Flask test client"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_success(client):
    """Successful test: Verifies that the route '/' responds with status code 200"""
    response = client.get("/")
    assert response.status_code == 200
    assert "La página ha sido cargada" in response.get_data(as_text=True)

def test_not_found(client):
    """Failed test: Tries to access a non-existent route"""
    response = client.get("/notfound")
    assert response.status_code == 404

def test_forzado():
    """Test that always fails intentionally"""
    assert False, "This test is designed to fail"