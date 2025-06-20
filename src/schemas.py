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


class IngredientInDrinkResponse(SQLModel):
    id: int
    name: str
    is_available: bool
    amount_ml: float


class DrinkCreate(SQLModel):
    name: str
    ingredients: Optional[List] = []


class DrinkUpdate(SQLModel):
    name: str
    ingredients: Optional[List] = []


class SimpleDrinkResponse(SQLModel):
    id: int
    name: str


class DrinkResponse(SQLModel):
    id: int
    name: str
    ingredients: List[IngredientInDrinkResponse]


class DrinkIngredientLinkBase(SQLModel):
    drink_id: int
    ingredient_id: int
    amount_ml: float
    unit: str = "ml"


class DrinkIngredientLinkCreate(DrinkIngredientLinkBase):
    pass


class DrinkIngredientLinkResponse(DrinkIngredientLinkBase):
    pass


class DrinkIngredientLinkUpdate(DrinkIngredientLinkBase):
    pass
