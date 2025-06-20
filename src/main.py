from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routers import drinks, ingredients, root, drink_ingredient_links
from .db import create_db_and_tables

if TYPE_CHECKING:
    from typing import AsyncGenerator, Any


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, Any]:

    create_db_and_tables()

    app.include_router(router=root.router, prefix="", tags=["Root"])
    app.include_router(
        router=ingredients.router, prefix="/ingredients", tags=["Ingredients"]
    )
    app.include_router(router=drinks.router, prefix="/drinks", tags=["Cocktails"])
    app.include_router(
        router=drink_ingredient_links.router, prefix="/links", tags=["Links"]
    )

    yield


app = FastAPI(lifespan=lifespan)
