from fastapi import APIRouter, status, HTTPException
from typing import List
from ..schemas import CocktailCreate, CocktailResponse, CocktailUpdate
from ..crud.cocktails import (
    get_cocktails_from_db,
    get_cocktail_by_id_from_db,
    get_cocktail_by_name_from_db,
    create_cocktail_in_db,
    update_cocktail_in_db,
)


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[CocktailResponse])
async def get_cocktails():
    cocktails = get_cocktails_from_db()
    return cocktails


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CocktailResponse)
async def get_cocktail_by_id(id: int):
    cocktail = get_cocktail_by_id_from_db(id)
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cocktail with id {id} not found",
        )
    return cocktail


@router.get(
    "/by-name/{name}", status_code=status.HTTP_200_OK, response_model=CocktailResponse
)
async def get_cocktail_by_name(name: str):
    cocktail = get_cocktail_by_name_from_db(name)
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cocktail with id {id} not found",
        )
    return cocktail


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CocktailResponse)
async def make_cocktail(new_cocktail: CocktailCreate):
    created_cocktail = create_cocktail_in_db(new_cocktail)
    return created_cocktail


@router.put(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=CocktailResponse
)
async def update_cocktail(id: int, updated_cocktail: CocktailUpdate):
    cocktail = get_cocktail_by_id_from_db(id)
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cocktail with id {id} not found",
        )
    updated_cocktail = update_cocktail_in_db(cocktail, updated_cocktail)
    return updated_cocktail
