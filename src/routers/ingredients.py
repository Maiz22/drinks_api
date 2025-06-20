from fastapi import APIRouter, status, HTTPException, Response
from typing import List
from ..schemas import IngredientCreate, IngredientResponse, IngredientUpdate
from ..crud.ingredients import (
    get_ingredients_from_db,
    get_ingredient_by_id_from_db,
    create_ingredient_in_db,
    update_ingredient_in_db,
    get_ingredient_by_name_from_db,
    delete_ingredient_in_db,
)


router = APIRouter()


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[IngredientResponse]
)
async def get_ingredients():
    ingredients = get_ingredients_from_db()
    return ingredients


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=IngredientResponse)
async def get_ingredient_by_id(id: int):
    ingredient = get_ingredient_by_id_from_db(id)
    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ingredient with id {id} not found",
        )
    return ingredient


@router.get(
    "/by-name/{name}", status_code=status.HTTP_200_OK, response_model=IngredientResponse
)
async def get_ingredient_by_name(name: str):
    ingredient = get_ingredient_by_name_from_db(name)
    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ingredient with name {name} not found",
        )
    return ingredient


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=IngredientResponse
)
async def add_ingredient(new_ingredient: IngredientCreate):
    new_ingredient = create_ingredient_in_db(new_ingredient)
    if new_ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Item already exists in DB"
        )
    return new_ingredient


@router.put(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=IngredientResponse
)
async def update_ingredient(id: int, updated_ingredient: IngredientUpdate):
    ingredient = get_ingredient_by_id_from_db(id)
    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ingredient with id {id} not found",
        )
    updated_ingredient = update_ingredient_in_db(ingredient, updated_ingredient)
    return updated_ingredient


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ingredient(id: int):
    drink = get_ingredient_by_id_from_db(id)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ingredient with id {id} not found",
        )
    delete_ingredient_in_db(drink)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
