from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Login route placeholder for 5Paisa"}
