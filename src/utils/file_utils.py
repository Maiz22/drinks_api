from __future__ import annotations
from typing import TYPE_CHECKING
import uuid
import os
import shutil
from pathlib import Path
from ..config.settings import settings, BASE_DIR

if TYPE_CHECKING:
    from fastapi import UploadFile


def save_file(file: UploadFile) -> str:
    """
    Takes an UploadFile instance. Sets a radnom name as a
    UUID. Creates and copies the file the filepath.
    Returns the filepath.
    """
    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    relpath = os.path.join(settings.img_upload_dir, filename)
    filepath = os.path.join(BASE_DIR, relpath)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return filename


def delete_file(filepath: str) -> None:
    """
    Take the dilepath as input and raises a value error if
    the file could not be found. Removes the file otherwise.
    """
    relpath = Path(filepath.lstrip("/\\"))
    filepath = os.path.join(BASE_DIR, relpath)
    print("\n", filepath)
    if not os.path.exists(filepath):
        raise ValueError("File not found")
    os.remove(filepath)
