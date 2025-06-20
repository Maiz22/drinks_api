import pytest
from fastapi.testclient import TestClient
from src.main import app

ROUTE = "/drinks"


def test_get_drinks_empty():
    with TestClient(app) as client:
        response = client.get(ROUTE)
        assert response.status_code == 200
        assert response.json() == []


def test_get_drink_by_id_not_found():
    with TestClient(app) as client:
        response = client.get(f"{ROUTE}/999")
        assert response.status_code == 404


def test_get_drink_by_name_not_found():
    with TestClient(app) as client:
        name = "drink_does_not_exist"
        response = client.get(f"{ROUTE}/by-name/{name}")
        assert response.status_code == 404


def test_create_drink():
    with TestClient(app) as client:
        payload = {"name": "TestDrink123", "img_url": ""}
        response = client.post(ROUTE, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "TestDrink123"
        assert "id" in data

        # Cleanup
        del_response = client.delete(f"{ROUTE}/{data['id']}")
        assert del_response.status_code == 204


@pytest.fixture
def create_drink_id():
    with TestClient(app) as client:
        payload = {"name": "TestDrinkToDelete", "img_url": ""}
        response = client.post(ROUTE, json=payload)
        data = response.json()
        yield data["id"]
        client.delete(f"{ROUTE}/{data['id']}")


@pytest.fixture
def create_drink_name():
    with TestClient(app) as client:
        payload = {"name": "TestDrinkToDelete", "img_url": ""}
        response = client.post(ROUTE, json=payload)
        data = response.json()
        yield data["name"]
        client.delete(f"{ROUTE}/{data['id']}")


def test_delete_drink(create_drink_id):
    with TestClient(app) as client:
        response = client.delete(f"{ROUTE}/{create_drink_id}")
        assert response.status_code == 204


def test_update_drink():
    with TestClient(app) as client:
        # create drink
        payload = {"name": "TestDrink123", "img_url": ""}
        response = client.post(ROUTE, json=payload)
        assert response.status_code == 201
        data = response.json()

        # update drink
        payload = {"name": "UpdateDrink123"}
        update_response = client.put(f"{ROUTE}/{data['id']}", json=payload)
        assert update_response.status_code == 201
        data = update_response.json()
        assert data["name"] == "UpdateDrink123"

        # delete drink
        client.delete(f"{ROUTE}/{data['id']}")


def test_get_drinks_success(create_drink_id):
    with TestClient(app) as client:
        response = client.get(f"{ROUTE}/")
        assert response.status_code == 200
        data = response.json()
        assert "id" in data[0]
        assert data[0]["name"] == "TestDrinkToDelete"
        assert data[0]["img_url"] == ""


def test_get_drink_by_id_success(create_drink_id):
    with TestClient(app) as client:
        response = client.get(f"{ROUTE}/{create_drink_id}")
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["name"] == "TestDrinkToDelete"
        assert data["img_url"] == ""


def test_get_drink_by_name_success(create_drink_name):
    with TestClient(app) as client:
        response = client.get(f"{ROUTE}/by-name/{create_drink_name}")
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["name"] == "TestDrinkToDelete"
        assert data["img_url"] == ""
