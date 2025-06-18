from sqlmodel import Session, select
from typing import List
from ..db import engine
from ..models import Cocktail
from ..schemas import CocktailCreate


def get_cocktails_from_db() -> List[Cocktail]:
    with Session(engine) as session:
        statement = select(Cocktail)
        result = session.exec(statement)
        cocktails = result.all()
    return cocktails


def get_cocktails_by_id_from_db(id: int) -> Cocktail:
    with Session(engine) as session:
        statement = select(Cocktail).where(Cocktail.id == id)
        result = session.exec(statement)
        cocktail = result.first()
    return cocktail


def create_cocktail(cocktail: CocktailCreate) -> Cocktail:
    new_cocktail = Cocktail(**cocktail.model_dump())
    with Session(engine) as session:
        session.add(new_cocktail)
        session.commit()
        session.refresh(new_cocktail)
    return new_cocktail
