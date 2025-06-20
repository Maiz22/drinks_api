from sqlmodel import Session, select
from typing import List
from sqlalchemy.exc import IntegrityError
import logging
from ..db import engine
from ..models import Ingredient
from ..schemas import IngredientCreate, IngredientUpdate

logger = logging.getLogger("uvicorn")


def get_ingredients_from_db() -> List[Ingredient]:
    with Session(engine) as session:
        statement = select(Ingredient)
        result = session.exec(statement)
        ingredients = result.all()
    return ingredients


def get_ingredient_by_id_from_db(id: int) -> Ingredient:
    with Session(engine) as session:
        statement = select(Ingredient).where(Ingredient.id == id)
        result = session.exec(statement)
        ingredient = result.first()
    return ingredient


def get_ingredient_by_name_from_db(name: str) -> Ingredient:
    with Session(engine) as session:
        statement = select(Ingredient).where(Ingredient.name == name)
        result = session.exec(statement)
        ingredient = result.first()
    return ingredient


def create_ingredient_in_db(ingredient: IngredientCreate) -> Ingredient:
    new_ingredient = Ingredient(**ingredient.model_dump())
    try:
        with Session(engine) as session:
            session.add(new_ingredient)
            session.commit()
            session.refresh(new_ingredient)
    except IntegrityError:
        logger.error("Element already exists in DB")
        return None
    return new_ingredient


def update_ingredient_in_db(
    ingredient: Ingredient, updated_ingredient: IngredientUpdate
) -> Ingredient:
    updated_ingredient = updated_ingredient.model_dump(exclude_unset=True)
    with Session(engine) as session:
        for key, value in updated_ingredient.items():
            setattr(ingredient, key, value)
            session.add(ingredient)
            session.commit()
            session.refresh(ingredient)
    return ingredient


def delete_ingredient_in_db(ingredient: Ingredient) -> None:
    with Session(engine) as session:
        session.delete(ingredient)
        session.commit()


def add_file_url_to_ingredient_in_db(ingredient: Ingredient, url: str) -> None:
    ingredient.img_url = url
    with Session(engine) as session:
        session.add(ingredient)
        session.commit()
        session.refresh(ingredient)
