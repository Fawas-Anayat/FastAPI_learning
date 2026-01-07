from pydantic import BaseModel
from schemas import User , Create_user
from fastapi import FastAPI , HTTPException , Depends
from typing import Optional 
from database import fake_users_db
from auth import get_hash_password ,authenticate_user ,create_access_token,get_current_active_user
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from datetime import timedelta


app=FastAPI()

@app.get("/health")
def health():
    return{
        "health":"ok",
        "is everything working fine":True
    }


@app.post("/signup",response_model=User ,status_code=200)
def signup(user: Create_user) -> Optional[Create_user]:
    if user.username in fake_users_db:
        raise HTTPException(status_code=401 , detail="user already exists")
    
    hashed_password=get_hash_password(user.password)
    new_user_id=len(fake_users_db)+101
    fake_users_db[user.username]={
        "user_id":new_user_id,
        "username":user.username,
        "email":user.email,
        "hashed_password":hashed_password,
        "disabled": False
    }
    return User(
        user_id=new_user_id,
        username=user.username,
        email=user.email,
    )


@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user=authenticate_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=401,detail="invalid username or password")
    access_token_expires=timedelta(minutes=20)
    access_token=create_access_token(
        data={"sub":user.username},expires_delta=access_token_expires
    )
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }


@app.get("/user/me",response_model=User)
def this_user(this_user:User=Depends(get_current_active_user)):
    return this_user