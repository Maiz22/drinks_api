import pytest
from fastapi.testclient import TestClient
from src.main import app


ROUTE = "/links"


@pytest.fixture
def create_ingredient_and_drink():
    with TestClient(app) as client:
        ingredient_payload = {"name": "TestIngredientToDelete", "is_available": True}
        ingredient_response = client.post("/ingredients", json=ingredient_payload)
        ingredient_data = ingredient_response.json()
        drink_payload = {"name": "TestDrinkToDelete", "img_url": ""}
        drink_response = client.post("/drinks", json=drink_payload)
        drink_data = drink_response.json()
        yield ingredient_data["id"], drink_data["id"]
        client.delete(f"ingredients/{ingredient_data['id']}")
        client.delete(f"drinks/{drink_data['id']}")


@pytest.fixture
def create_ingredient_drink_link():
    with TestClient(app) as client:
        # crient drink and ingredient
        ingredient_payload = {"name": "TestIngredientToDelete", "is_available": True}
        ingredient_response = client.post("/ingredients", json=ingredient_payload)
        ingredient_data = ingredient_response.json()
        drink_payload = {"name": "TestDrinkToDelete", "img_url": ""}
        drink_response = client.post("/drinks", json=drink_payload)
        drink_data = drink_response.json()

        # create link
        payload = {
            "drink_id": drink_data["id"],
            "ingredient_id": ingredient_data["id"],
            "amount_ml": 100,
            "unit": "ml",
        }
        with TestClient(app) as client:
            response = client.post(ROUTE, json=payload)
            assert response.status_code == 201
            data = response.json()

        yield data["drink_id"], data["ingredient_id"]

        # cleanup
        client.delete(f"ingredients/{ingredient_data['id']}")
        client.delete(f"drinks/{drink_data['id']}")
        client.delete(f"{ROUTE}/{data["drink_id"]}/{data["ingredient_id"]}")


def test_create_link(create_ingredient_and_drink):
    ingredient_id, drink_id = create_ingredient_and_drink
    payload = {
        "drink_id": drink_id,
        "ingredient_id": ingredient_id,
        "amount_ml": 100,
        "unit": "ml",
    }
    with TestClient(app) as client:
        response = client.post(ROUTE, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["drink_id"] == drink_id
        assert data["ingredient_id"] == ingredient_id
        assert data["amount_ml"] == 100
        assert data["unit"] == "ml"

        # delete for clearup
        del_response = client.delete(
            f"{ROUTE}/{data["drink_id"]}/{data["ingredient_id"]}"
        )
        assert del_response.status_code == 204


def test_delete_link(create_ingredient_drink_link):
    drink_id, ingredient_id = create_ingredient_drink_link
    with TestClient(app) as client:
        response = client.delete(f"{ROUTE}/{drink_id}/{ingredient_id}")
        assert response.status_code == 204


def test_update_link(create_ingredient_drink_link):
    drink_id, ingredient_id = create_ingredient_drink_link
    payload = {
        "drink_id": drink_id,
        "ingredient_id": ingredient_id,
        "amount_ml": 123,
        "unit": "cl",
    }
    with TestClient(app) as client:
        response = client.put(f"{ROUTE}/{drink_id}/{ingredient_id}", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["drink_id"] == drink_id
        assert data["ingredient_id"] == ingredient_id
        assert data["amount_ml"] == 123
        assert data["unit"] == "cl"
