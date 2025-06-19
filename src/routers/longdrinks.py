from fastapi import APIRouter, status, HTTPException
from typing import List
from ..schemas import LongdrinkCreate, LongdrinkResponse, LongdrinkUpdate
from ..crud.longdrinks import (
    get_longdrinks_from_db,
    get_longdrink_by_id_from_db,
    get_longdrink_by_name_from_db,
    update_longdrink_in_db,
    create_longdrink_in_db,
)


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[LongdrinkResponse])
def get_longdrinks():
    longdrinks = get_longdrinks_from_db()
    return longdrinks


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=LongdrinkResponse)
def get_longdrink_by_id(id: int):
    longdrink = get_longdrink_by_id_from_db(id)
    if longdrink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cocktail with id {id} not found",
        )
    return longdrink


@router.get(
    "/by-name/{name}", status_code=status.HTTP_200_OK, response_model=LongdrinkResponse
)
def get_longdrink_by_name(name: str):
    longdrink = get_longdrink_by_name_from_db(name)
    if longdrink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cocktail with id {id} not found",
        )
    return longdrink


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=LongdrinkResponse)
def make_longdrink(new_longdrink: LongdrinkCreate):
    created_longdrink = create_longdrink_in_db(new_longdrink)
    return created_longdrink


@router.put(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=LongdrinkResponse
)
async def update_longdrink(id: int, updated_longdrink: LongdrinkUpdate):
    longdrink = get_longdrink_by_id_from_db(id)
    if longdrink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cocktail with id {id} not found",
        )
    updated_longdrink = update_longdrink_in_db(longdrink, updated_longdrink)
    return updated_longdrink
