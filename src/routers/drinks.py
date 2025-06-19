from fastapi import APIRouter, status, HTTPException, Response
from typing import List
from ..schemas import DrinkCreate, DrinkResponse, DrinkUpdate
from ..crud.drinks import (
    get_drinks_from_db,
    get_drink_by_id_from_db,
    get_drink_by_name_from_db,
    create_drink_in_db,
    update_drink_in_db,
    delete_drink_in_db,
)


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[DrinkResponse])
async def get_drinks():
    drinks = get_drinks_from_db()
    return drinks


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=DrinkResponse)
async def get_drink_by_id(id: int):
    drink = get_drink_by_id_from_db(id)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drink with id {id} not found",
        )
    return drink


@router.get(
    "/by-name/{name}", status_code=status.HTTP_200_OK, response_model=DrinkResponse
)
async def get_drink_by_name(name: str):
    drink = get_drink_by_name_from_db(name)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drink with name {name} not found",
        )
    return drink


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DrinkResponse)
async def make_drink(new_drink: DrinkCreate):
    created_drink = create_drink_in_db(new_drink)
    if created_drink is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Item already exists in DB"
        )
    return created_drink


@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=DrinkResponse)
async def update_drink(id: int, updated_drink: DrinkUpdate):
    drink = get_drink_by_id_from_db(id)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drink with id {id} not found",
        )
    updated_drink = update_drink_in_db(drink, updated_drink)
    return updated_drink


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_drink(id: int):
    drink = get_drink_by_id_from_db(id)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drink with id {id} not found",
        )
    delete_drink_in_db(drink)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
