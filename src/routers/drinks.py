from fastapi import APIRouter, status, HTTPException, Response, UploadFile
from typing import List
from ..utils.file_utils import save_file, delete_file
from ..config.settings import settings
from ..schemas import (
    DrinkCreate,
    DrinkResponse,
    DrinkUpdate,
    SimpleDrinkResponse,
    IngredientInDrinkResponse,
)
from ..crud.drinks import (
    get_drinks_from_db,
    get_drink_by_id_from_db,
    get_drink_by_name_from_db,
    create_drink_in_db,
    update_drink_in_db,
    delete_drink_in_db,
    add_file_url_to_drink_in_db,
)


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[DrinkResponse])
async def get_drinks():
    drinks = get_drinks_from_db()

    return [
        DrinkResponse(
            id=drink.id,
            name=drink.name,
            ingredients=[
                IngredientInDrinkResponse(
                    id=link.ingredient.id,
                    name=link.ingredient.name,
                    is_available=link.ingredient.is_available,
                    amount_ml=link.amount_ml,
                    unit=link.unit,
                )
                for link in drink.ingredient_links
            ],
            img_url=drink.img_url,
        )
        for drink in drinks
    ]


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=DrinkResponse)
async def get_drink_by_id(id: int):
    drink = get_drink_by_id_from_db(id)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drink with id {id} not found",
        )
    return DrinkResponse(
        id=drink.id,
        name=drink.name,
        ingredients=[
            IngredientInDrinkResponse(
                id=link.ingredient.id,
                name=link.ingredient.name,
                is_available=link.ingredient.is_available,
                amount_ml=link.amount_ml,
                unit=link.unit,
            )
            for link in drink.ingredient_links
        ],
        img_url=drink.img_url,
    )


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
    return DrinkResponse(
        id=drink.id,
        name=drink.name,
        ingredients=[
            IngredientInDrinkResponse(
                id=link.ingredient.id,
                name=link.ingredient.name,
                is_available=link.ingredient.is_available,
                amount_ml=link.amount_ml,
                unit=link.unit,
            )
            for link in drink.ingredient_links
        ],
        img_url=drink.img_url,
    )


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=SimpleDrinkResponse
)
async def make_drink(new_drink: DrinkCreate):
    created_drink = create_drink_in_db(new_drink)
    if created_drink is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Item already exists in DB"
        )
    return created_drink


@router.put(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=SimpleDrinkResponse
)
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
    if drink.img_url.strip() != "":
        delete_file(drink.img_url.strip())
    delete_drink_in_db(drink)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{id}/upload-image", status_code=status.HTTP_201_CREATED)
def upload_image(id: int, file: UploadFile):

    # check if the drink id exists in the db
    drink = get_drink_by_id_from_db(id)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drink with id {id} not found",
        )

    filename = save_file(file)

    # add file url to the drink db
    url = f"/{settings.img_upload_dir}/{filename}"
    add_file_url_to_drink_in_db(drink, url)

    return {"filename": filename, "url": url}
