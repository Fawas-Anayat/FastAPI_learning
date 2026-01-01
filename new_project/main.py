from fastapi import FastAPI
from database import database
from schemas import UserCreate, UserOut
import crud

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate):
    return await crud.create_user(user.name, user.email)

@app.get("/users/", response_model=list[UserOut])
async def read_users():
    return await crud.get_users()
