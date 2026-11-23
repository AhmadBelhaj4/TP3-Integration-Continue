"""Tests unitaires pour l'application FastAPI."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """Teste le endpoint racine."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}


def test_greeting():
    """Teste le endpoint greeting."""
    response = client.get("/greeting?name=Alice")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, Alice"
    assert data["developer"] == "Dev2"
    assert "hostname" in data
    assert "IP" in data


def test_addition():
    """Teste l'addition."""
    response = client.get("/addition?a=7&b=3")
    assert response.status_code == 200
    assert response.json() == {"result a+b": 10, "developer": "Dev1"}


def test_soustraction_positive():
    """Teste la soustraction avec résultat positif."""
    response = client.get("/soustraction?a=10&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 6, "developer": "Dev1"}


def test_soustraction_negative():
    """Teste la soustraction avec résultat négatif."""
    response = client.get("/soustraction?a=4&b=10")
    assert response.status_code == 200
    assert response.json() == {"result": -6, "developer": "Dev1"}


def test_soustraction_zero():
    """Teste la soustraction donnant zero."""
    response = client.get("/soustraction?a=5&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 0, "developer": "Dev1"}


def test_multiply():
    """Teste la multiplication POST."""
    response = client.post("/multiply", json={"a": 4.0, "b": 2.5})
    assert response.status_code == 200
    assert response.json() == {"result": 10.0, "developer": "Dev1"}


def test_divide_success():
    """Teste la division normale POST."""
    response = client.post("/divide", json={"a": 10.0, "b": 2.0})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0, "developer": "Dev2"}


def test_divide_by_zero():
    """Teste l'erreur 400 lors d'une division par zero."""
    response = client.post("/divide", json={"a": 10.0, "b": 0.0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Erreur: Division par zero impossible."


def test_remove_item_success():
    """Teste la suppression d'un element existant."""
    response = client.delete("/remove/1")
    assert response.status_code == 200
    assert "supprime" in response.json()["message"]


def test_remove_item_not_found():
    """Teste la suppression d'un element inexistant (404)."""
    response = client.delete("/remove/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Element non trouve"