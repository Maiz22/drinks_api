import pytest
from fastapi.testclient import TestClient
from src.main import app

ROUTE = "/ingredients"


def test_get_ingredients_empty():
    with TestClient(app) as client:
        response = client.get(ROUTE)
        response.status_code == 200
        response.content == []


def test_get_ingredient_by_id_not_fount():
    with TestClient(app) as client:
        response = client.get(f"{ROUTE}/999")
        response.status_code == 404


def test_get_ingredient_by_name_not_fount():
    with TestClient(app) as client:
        name = "ingredient_does_not_exist"
        response = client.get(f"{ROUTE}/by-name/{name}")
        response.status_code == 404


def test_create_ingredient():
    with TestClient(app) as client:
        payload = {"name": "Test123", "is_available": True}
        response = client.post(ROUTE, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test123"
        assert data["is_available"] is True
        assert "id" in data

        # Cleanup
        del_response = client.delete(f"{ROUTE}/{data['id']}")
        assert del_response.status_code == 204


@pytest.fixture
def create_ingredient():
    with TestClient(app) as client:
        payload = {"name": "TestToDelete", "is_available": True}
        response = client.post(ROUTE, json=payload)
        data = response.json()
        yield data["id"]
        client.delete(f"{ROUTE}/{data['id']}")


def test_delete_ingredient(create_ingredient):
    with TestClient(app) as client:
        response = client.delete(f"{ROUTE}/{create_ingredient}")
        assert response.status_code == 204


def test_update_ingredient():
    with TestClient(app) as client:
        # create ingredient
        payload = {"name": "Test123", "is_available": True}
        response = client.post(ROUTE, json=payload)
        assert response.status_code == 201
        data = response.json()

        # update ingredient
        payload = {"name": "Update123", "is_available": False}
        update_response = client.put(f"{ROUTE}/{data["id"]}", json=payload)
        assert update_response.status_code == 201
        data = update_response.json()
        assert data["name"] == "Update123"
        assert data["is_available"] is False

        # delete ingredient
        client.delete(f"{ROUTE}/{data['id']}")
