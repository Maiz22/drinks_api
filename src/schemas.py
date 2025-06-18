from sqlmodel import SQLModel
from typing import List, Optional


class CocktailCreate(SQLModel):
    name: str
    ingredients: List


class CocktailResponse(SQLModel):
    id: int
    name: str
    ingredients: List


class LongdrinkCreate(SQLModel):
    name: str
    ingredients: List


class LongdrinkResponse(SQLModel):
    id: int
    name: str
    ingredients: List


class DrinkCreate(SQLModel):
    id: int
    name: str
    is_available: Optional[bool] = True


class DrinkResponse(SQLModel):
    name: str
    is_available: bool
