from sqlmodel import Session, select
from typing import List
from ..db import engine
from ..models import Cocktail
from ..schemas import CocktailCreate, CocktailUpdate


def get_cocktails_from_db() -> List[Cocktail]:
    with Session(engine) as session:
        statement = select(Cocktail)
        result = session.exec(statement)
        cocktails = result.all()
    return cocktails


def get_cocktail_by_id_from_db(id: int) -> Cocktail:
    with Session(engine) as session:
        statement = select(Cocktail).where(Cocktail.id == id)
        result = session.exec(statement)
        cocktail = result.first()
    return cocktail


def get_cocktail_by_name_from_db(name: str) -> Cocktail:
    with Session(engine) as session:
        statement = select(Cocktail).where(Cocktail.name == name)
        result = session.exec(statement)
        cocktail = result.first()
    return cocktail


def create_cocktail_in_db(cocktail: CocktailCreate) -> Cocktail:
    new_cocktail = Cocktail(**cocktail.model_dump())
    with Session(engine) as session:
        session.add(new_cocktail)
        session.commit()
        session.refresh(new_cocktail)
    return new_cocktail


def update_cocktail_in_db(
    cocktail: Cocktail, updated_cocktail: CocktailUpdate
) -> Cocktail:
    updated_cocktail = updated_cocktail.model_dump(exclude_unset=True)
    with Session(engine) as session:
        for key, value in updated_cocktail.items():
            setattr(cocktail, key, value)
            session.add(cocktail)
            session.commit()
            session.refresh(cocktail)
    return cocktail
