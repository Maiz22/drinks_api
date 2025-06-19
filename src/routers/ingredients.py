from fastapi import APIRouter, status
from typing import List
from ..schemas import IngredientCreate, IngredientResponse, IngredientUpdate


router = APIRouter()


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[IngredientResponse]
)
def get_ingredients():
    # get all ingredients from db
    # respond according to the response model schema
    pass


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=IngredientResponse)
def get_ingredient_by_id(id: int):
    # get ingredient by id from db
    # respond according to the response model schema
    pass


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=IngredientResponse
)
def add_ingredient(ingredient: IngredientCreate):
    # Create ingredient in DB
    # respond according to the response model schema
    pass


@router.put(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=IngredientResponse
)
def update_ingredient(id: int, updated_ingredient: IngredientUpdate):
    pass
