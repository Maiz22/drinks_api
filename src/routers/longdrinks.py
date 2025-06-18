from fastapi import APIRouter, status
from ..schemas import LongdrinkCreate, LongdrinkResponse
from typing import List


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[LongdrinkResponse])
def get_longdrinks():
    # get all longdrinks from db
    # respond according to the response model schema
    pass


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=LongdrinkResponse)
def get_longdrink_by_id(id: int):
    # get longdrink by id from db
    # respond according to the response model schema
    pass


@router.get(
    "/by-name/{name}", status_code=status.HTTP_200_OK, response_model=LongdrinkResponse
)
def get_longdrink_by_name(name: str):
    pass


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=LongdrinkResponse)
def make_longdrink(longdrink: LongdrinkCreate):
    # check id and name
    # arbitration logic

    # get recipe

    # check available drinks
    # raise exception if drink unavailable
    pass
