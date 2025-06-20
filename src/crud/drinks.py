from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from typing import List
from sqlalchemy.exc import IntegrityError
import logging
from ..db import engine
from ..models import Drink, DrinkIngredientLink
from ..schemas import DrinkCreate, DrinkUpdate


logger = logging.getLogger("uvicorn")


def get_drinks_from_db() -> List[Drink]:
    with Session(engine) as session:
        statement = select(Drink).options(
            selectinload(Drink.ingredient_links).selectinload(
                DrinkIngredientLink.ingredient
            )
        )
        result = session.exec(statement)
        drinks = result.all()
    return drinks


def get_drink_by_id_from_db(id: int) -> Drink:
    with Session(engine) as session:
        statement = (
            select(Drink)
            .where(Drink.id == id)
            .options(
                selectinload(Drink.ingredient_links).selectinload(
                    DrinkIngredientLink.ingredient
                )
            )
        )
        result = session.exec(statement)
        drink = result.first()
    return drink


def get_drink_by_name_from_db(name: str) -> Drink:
    with Session(engine) as session:
        statement = (
            select(Drink)
            .where(Drink.name == name)
            .options(
                selectinload(Drink.ingredient_links).selectinload(
                    DrinkIngredientLink.ingredient
                )
            )
        )
        result = session.exec(statement)
        drink = result.first()
    return drink


def create_drink_in_db(drink: DrinkCreate) -> Drink:
    new_drink = Drink(**drink.model_dump())
    try:
        with Session(engine) as session:
            session.add(new_drink)
            session.commit()
            session.refresh(new_drink)
    except IntegrityError as e:
        logger.error("Element already exists in DB")
        return None
    return new_drink


def update_drink_in_db(drink: Drink, updated_drink: DrinkUpdate) -> Drink:
    updated_drink = updated_drink.model_dump(exclude_unset=True)
    with Session(engine) as session:
        for key, value in updated_drink.items():
            setattr(drink, key, value)
            session.add(drink)
            session.commit()
            session.refresh(drink)
    return drink


def delete_drink_in_db(drink: Drink) -> None:
    with Session(engine) as session:
        session.delete(drink)
        session.commit()


def add_file_url_to_drink_in_db(drink: Drink, url: str) -> None:
    drink.img_url = url
    with Session(engine) as session:
        session.add(drink)
        session.commit()
        session.refresh(drink)
