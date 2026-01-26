from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db import get_db
from models import AuthorM

SECRET_KEY="mysecertkey"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def authinticate_user(password : str , email : str ,db:Session):
    user=db.query(AuthorM).filter(AuthorM.email == email).first()
    if not user:
        return False
    
    if not verify_password(password, user.password):
        return False
    
    return user  



def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# function to create the access token
def create_access_token(data: AuthorM, expires_delta: Optional[timedelta] = None):
    data_dic = {
        "id" : data.id ,
        "name" : data.name ,
        "email" : data.email ,
    }

    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    data_dic.update({"exp": expire})
    
    encoded_jwt = jwt.encode(data_dic, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    

def get_current_user(
        token : str = Depends(oauth2_scheme) ,
        db : Session = Depends(get_db)
):
    payload = verify_token(token)
    user_email = payload.get("email")
    user = db.query(AuthorM).filter(AuthorM.email == user_email).first()
    if not user :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND , detail="no user found with this information"
        )
    return user
    

