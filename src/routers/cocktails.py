from fastapi import APIRouter, status
from ..schemas import CocktailCreate, CocktailResponse
from typing import List


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[CocktailResponse])
def get_cocktails():
    # get all cocktails from db
    # respond list of Cocktails according to the response model
    pass


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CocktailResponse)
def get_cocktail_by_id(id: int):
    # get cocktail by id
    # response according to response_model schema
    pass


@router.get(
    "/by-name/{name}", status_code=status.HTTP_200_OK, response_model=CocktailResponse
)
def get_cocktail_by_name(name: str):
    # get cocktail by name
    # response according to response_model schema
    pass


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CocktailResponse)
def make_cocktail(cocktail: CocktailCreate):
    # check id and name
    # arbitration logic

    # check available drinks
    # raise exception if drink unavailable
    pass
