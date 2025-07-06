from fastapi import FastAPI
from app.routes import auth

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth")

@app.get("/")
def read_root():
    return {"msg": "Algo Trading Backend Running"}
