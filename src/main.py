from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from .config.settings import settings
from .routers import drinks, ingredients, root, drink_ingredient_links
from .db import create_db_and_tables

if TYPE_CHECKING:
    from typing import AsyncGenerator, Any


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, Any]:

    # make sure that the static/img upload dir exists
    os.makedirs(settings.img_upload_dir, exist_ok=True)

    app.mount("/static", StaticFiles(directory="static"), name="static")

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


origins = [
    "http://localhost:5173",
]

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Accept requests from these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
