from sqlmodel import SQLModel
from typing import List, Optional


class IngredientCreate(SQLModel):
    id: int
    name: str
    is_available: Optional[bool] = True


class IngredientResponse(SQLModel):
    name: str
    is_available: bool


class IngredientUpdate(SQLModel):
    id: int
    name: str
    is_available: Optional[bool] = True


class CocktailCreate(SQLModel):
    name: str
    ingredients: List


class CocktailUpdate(SQLModel):
    name: str
    ingredients: List


class CocktailResponse(SQLModel):
    id: int
    name: str
    ingredients: List[IngredientResponse] = []


class LongdrinkCreate(SQLModel):
    name: str
    ingredients: List


class LongdrinkResponse(SQLModel):
    id: int
    name: str
    ingredients: List[IngredientResponse] = []


class LongdrinkUpdate(SQLModel):
    name: str
    ingredients: List
