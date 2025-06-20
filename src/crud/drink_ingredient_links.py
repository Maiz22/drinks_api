from sqlmodel import Session, select
from typing import List
from sqlalchemy.exc import IntegrityError
import logging
from ..db import engine
from ..models import DrinkIngredientLink
from ..schemas import DrinkIngredientLinkCreate, DrinkIngredientLinkUpdate

logger = logging.getLogger("uvicorn")


def get_link_by_ids_from_db(ingredient_id: int, drink_id: int) -> DrinkIngredientLink:
    with Session(engine) as session:
        statement = select(DrinkIngredientLink).where(
            (DrinkIngredientLink.drink_id == drink_id)
            & (DrinkIngredientLink.ingredient_id == ingredient_id)
        )
        link = session.exec(statement).first()
    return link


def create_link_in_db(new_link: DrinkIngredientLinkCreate) -> DrinkIngredientLink:
    new_link = DrinkIngredientLink(**new_link.model_dump())
    try:
        with Session(engine) as session:
            session.add(new_link)
            session.commit()
            session.refresh(new_link)
    except IntegrityError as e:
        logger.error("Link already exists. Update Link instead.")
        return None
    return new_link


def update_link_in_db(
    link: DrinkIngredientLink, updated_link: DrinkIngredientLinkUpdate
) -> DrinkIngredientLink:
    updated_link = updated_link.model_dump(exclude_unset=True)
    with Session(engine) as session:
        for key, value in updated_link.items():
            setattr(link, key, value)
            session.add(link)
            session.commit()
            session.refresh(link)
    return link


def delete_link_in_db(link: DrinkIngredientLink) -> None:
    with Session(engine) as session:
        session.delete(link)
        session.commit()
