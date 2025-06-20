from fastapi import APIRouter, status, HTTPException, Response
from ..schemas import (
    DrinkIngredientLinkCreate,
    DrinkIngredientLinkUpdate,
    DrinkIngredientLinkResponse,
)
from ..crud.ingredients import get_ingredient_by_id_from_db
from ..crud.drinks import get_drink_by_id_from_db
from ..crud.drink_ingredient_links import (
    create_link_in_db,
    get_link_by_ids_from_db,
    update_link_in_db,
    delete_link_in_db,
)


router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=DrinkIngredientLinkResponse
)
def create_link(link: DrinkIngredientLinkCreate):
    ingredient = get_ingredient_by_id_from_db(link.ingredient_id)
    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ingredient with id {id} not found",
        )
    drink = get_drink_by_id_from_db(link.drink_id)
    if drink is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drink with id {id} not found",
        )
    created_link = create_link_in_db(link)
    if created_link is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Link already exists in DB. Update Link instead",
        )
    return created_link


@router.put(
    "/{id}",
    status_code=status.HTTP_201_CREATED,
    response_model=DrinkIngredientLinkResponse,
)
def update_link(id: int, link: DrinkIngredientLinkUpdate):
    link_to_be_updated = get_link_by_ids_from_db(link.ingredient_id, link.drink_id)
    if link_to_be_updated is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Link does not exist in DB",
        )
    new_link = update_link_in_db(link_to_be_updated, link)
    return new_link


@router.delete("/{drink_id}/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_link(ingredient_id, drink_id):
    link = get_link_by_ids_from_db(ingredient_id, drink_id)
    if link is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Link does not exist in DB",
        )
    delete_link_in_db(link)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
