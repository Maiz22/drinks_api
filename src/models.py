from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class DrinkIngredientLink(SQLModel, table=True):
    __tablename__ = "drinkingredientlinks"
    drink_id: Optional[int] = Field(
        default=None, foreign_key="drinks.id", primary_key=True
    )
    ingredient_id: Optional[int] = Field(
        default=None, foreign_key="ingredients.id", primary_key=True
    )
    amount_ml: float
    unit: str = "ml"

    drink: Optional["Drink"] = Relationship(back_populates="ingredient_links")
    ingredient: Optional["Ingredient"] = Relationship(back_populates="drink_links")


class Drink(SQLModel, table=True):
    __tablename__ = "drinks"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False, unique=True)
    ingredient_links: List[DrinkIngredientLink] = Relationship(back_populates="drink")


class Ingredient(SQLModel, table=True):
    __tablename__ = "ingredients"
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)
    is_available: bool = Field(nullable=False, default=True)
    drink_links: List[DrinkIngredientLink] = Relationship(back_populates="ingredient")
