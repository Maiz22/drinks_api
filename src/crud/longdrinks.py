from sqlmodel import Session, select
from typing import List
from ..db import engine
from ..models import Longdrink
from ..schemas import LongdrinkCreate, LongdrinkUpdate


def get_longdrinks_from_db() -> List[Longdrink]:
    with Session(engine) as session:
        statement = select(Longdrink)
        result = session.exec(statement)
        longdrinks = result.all()
    return longdrinks


def get_longdrink_by_id_from_db(id: int) -> Longdrink:
    with Session(engine) as session:
        statement = select(Longdrink).where(Longdrink.id == id)
        result = session.exec(statement)
        longdrink = result.first()
    return longdrink


def get_longdrink_by_name_from_db(name: str) -> Longdrink:
    with Session(engine) as session:
        statement = select(Longdrink).where(Longdrink.name == name)
        result = session.exec(statement)
        longdrink = result.first()
    return longdrink


def create_longdrink_in_db(longdrink: LongdrinkCreate) -> Longdrink:
    new_longdrink = Longdrink(**longdrink.model_dump())
    with Session(engine) as session:
        session.add(new_longdrink)
        session.commit()
        session.refresh(new_longdrink)
    return new_longdrink


def update_longdrink_in_db(
    longdrink: Longdrink, updated_longdrink: LongdrinkUpdate
) -> Longdrink:
    updated_longdrink = updated_longdrink.model_dump(exclude_unset=True)
    with Session(engine) as session:
        for key, value in updated_longdrink.items():
            setattr(longdrink, key, value)
            session.add(longdrink)
            session.commit()
            session.refresh(longdrink)
    return longdrink
