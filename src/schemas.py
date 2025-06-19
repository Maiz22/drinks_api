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


class DrinkCreate(SQLModel):
    name: str
    ingredients: List


class DrinkUpdate(SQLModel):
    name: str
    ingredients: List


class DrinkResponse(SQLModel):
    id: int
    name: str
    ingredients: List[IngredientResponse] = []
