from fastapi import APIRouter, status


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def welcome_page():
    return {"message": "Welcome to the Drink Mixer API"}
