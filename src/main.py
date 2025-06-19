from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routers import ingredients, root, cocktails
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
    app.include_router(router=cocktails.router, prefix="/cocktails", tags=["Cocktails"])
    # app.include_router(
    #    router=longdrinks.router, prefix="/longdrinks", tags=["Longdrinks"]
    # )

    yield


app = FastAPI(lifespan=lifespan)
