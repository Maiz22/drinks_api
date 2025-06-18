from fastapi import APIRouter, status
from typing import List
from ..schemas import DrinkCreate, DrinkResponse


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[DrinkResponse])
def get_drinks():
    # get all drinks from db
    # respond according to the response model schema
    pass


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=DrinkResponse)
def get_drink_by_id(id: int):
    # get drink by id from db
    # respond according to the response model schema
    pass


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DrinkResponse)
def add_drink(drink: DrinkCreate):
    # Create drink in DB
    # respond according to the response model schema
    pass
