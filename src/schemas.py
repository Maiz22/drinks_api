from sqlmodel import SQLModel
from typing import List, Optional


class IngredientCreate(SQLModel):
    name: str
    is_available: Optional[bool] = True


class IngredientResponse(SQLModel):
    id: int
    name: str
    is_available: bool


class IngredientUpdate(SQLModel):
    name: str
    is_available: Optional[bool] = True


class DrinkCreate(SQLModel):
    name: str
    ingredients: Optional[List] = []


class DrinkUpdate(SQLModel):
    name: str
    ingredients: Optional[List] = []


class DrinkResponse(SQLModel):
    id: int
    name: str
    ingredients: List[IngredientResponse] = []
