from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class Drink(SQLModel, table=True):
    __tablename__ = "drinks"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False)
    is_available: bool = Field(nullable=False, default=True)


class Ingredient(SQLModel, table=True):
    __tablename__ = "ingredients"
    drink_id: int = Field(primary_key=True, foreign_key="drinks.id", ondelete="CASCADE")
    amount: float = Field(nullable=False)
    cocktail: Optional["Cocktail"] = Relationship(back_populates="ingredients")
    longdrink: Optional["Longdrink"] = Relationship(back_populates="ingredients")


class Cocktail(SQLModel, table=True):
    __tablename__ = "cocktails"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False)
    ingredients: List[Ingredient] = Relationship(back_populates="cocktails")


class Longdrink(SQLModel, table=True):
    __tablename__ = "longdrinks"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False)


ingredients: List[Ingredient] = Relationship(back_populates="longdrinks")
