from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class CocktailIngredientLink(SQLModel, table=True):
    cocktail_id: Optional[int] = Field(
        default=None, foreign_key="cocktails.id", primary_key=True
    )
    ingredient_id: Optional[int] = Field(
        default=None, foreign_key="ingredients.id", primary_key=True
    )
    amount_ml: float
    unit: str = "ml"

    cocktail: Optional["Cocktail"] = Relationship(back_populates="ingredient_links")
    ingredient: Optional["Ingredient"] = Relationship(back_populates="cocktail_links")


class Cocktail(SQLModel, table=True):
    __tablename__ = "cocktails"
    id: int | None = Field(primary_key=True, nullable=False, default=None)
    name: str = Field(nullable=False, unique=True)
    ingredient_links: List[CocktailIngredientLink] = Relationship(
        back_populates="cocktail"
    )


class Ingredient(SQLModel, table=True):
    __tablename__ = "ingredients"
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)
    is_available: bool = Field(nullable=False, default=True)
    cocktail_links: List[CocktailIngredientLink] = Relationship(
        back_populates="ingredient"
    )


# class LongdrinkIngredientLink(SQLModel, table=True):
#    longdrink_id: Optional[int] = Field(
#        default=None, foreign_key="longdrinks.id", primary_key=True
#    )
#    ingredient_id: Optional[int] = Field(
#        default=None, foreign_key="ingredients.id", primary_key=True
#    )
#    amount_ml: float
#    unit: str = "ml"
#
#    longdrink: Optional["Longdrink"] = Relationship(back_populates="ingredient_links")
#    ingredient: Optional["Ingredient"] = Relationship()
#
#
# class Longdrink(SQLModel, table=True):
#    __tablename__ = "longdrinks"
#    id: int | None = Field(primary_key=True, nullable=False, default=None)
#    name: str = Field(nullable=False, unique=True)
#    ingredient_link: List["Ingredient"] = Relationship(
#        back_populates="longdrinks", link_model=LongdrinkIngredientLink
#    )
