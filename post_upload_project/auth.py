from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db import get_db
from models import AuthorM , RefreshToken
import secrets

SECRET_KEY="mysecertkey"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRES_DAYS = 7

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

# function to create the refresh token
# this function just creates the token , for storing the token to the database we need to first hash the token and then separately make a new funvton that will do the complete implemenetation of saving the refresh token to the database

def create_refresh_token(data : AuthorM , db:Session = Depends(get_db)):
    now =  datetime.utcnow()
    expire= datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRES_DAYS)
    payload = {
        "sub": data.name,          
        "iat": now,               
        "exp": expire,            
        "user_id": data.id,       
        "type": "refresh",       
        "jti": secrets.token_urlsafe(32)  
    }

    encoded_ref_token = jwt.encode(payload , SECRET_KEY , algorithm=ALGORITHM)
    store_refresh_token(data , encoded_ref_token, db)
    return encoded_ref_token


def store_refresh_token(data : AuthorM , encoded_ref_tokn : RefreshToken , db : Session):

    payload = jwt.decode(encoded_ref_tokn, SECRET_KEY, algorithms=[ALGORITHM])
    jti = payload.get("jti")
    iat = payload.get("iat")
    expires_at = datetime.fromtimestamp(payload.get("exp"))
    token_hash = pwd_context.hash(encoded_ref_tokn)
    
    db_token = RefreshToken(
        user_id=data.id,
        token=token_hash,
        expires_at=expires_at ,
        created_at = iat
    )
    
    db.add(db_token)
    db.commit()
    

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


def create_tokens(user: AuthorM, db: Session) -> dict:

    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user,db)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

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
    

