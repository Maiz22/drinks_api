from sqlmodel import SQLModel, Field
from typing import List


class Drink(SQLModel, table=True):
    __tablename__ = "drinks"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False)
    is_available: bool = Field(nullable=False, default=True)


class Ingredient(SQLModel, table=True):
    __tablename__ = "ingredients"
    drink_id: int = Field(primary_key=True, foreign_key="drink.id", ondelete="CASCADE")
    amount: float = Field(nullable=False)


class Cocktail(SQLModel, table=True):
    __tablename__ = "cocktails"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False)
    ingedients: List[Ingredient]


class Longdrink(SQLModel, table=True):
    __tablename__ = "longdrinks"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False)
    ingedients: List[Ingredient]
