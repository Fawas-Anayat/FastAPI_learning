from fastapi.security import OAuth2PasswordBearer 
from passlib.context import CryptContext
from typing import Optional
from schemas import UserinDB , TokenData
from database import fake_users_db
from datetime import timedelta ,datetime
from jose import JWTError , jwt
from fastapi import Depends , status , HTTPException

SECRAT_KEY="asdjkxrgsenfgedfxb"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=20

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")


def get_user(username:str) -> Optional[UserinDB]:
    if username in fake_users_db:
        user_dict=fake_users_db[username]
        return UserinDB(**user_dict)
    return None

def verify_password(plain_password:str,hashed_password:str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)


def get_hash_password(plain_password:str):
    return pwd_context.hash(plain_password)

def authenticate_user(user_name,password):
    user=get_user(user_name)
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user

def create_access_token(data:dict,expires_delta:Optional[timedelta]= None) -> str:
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow() + expires_delta
    else:
        expire=datetime.utcnow() + timedelta(minutes=20)

    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode , SECRAT_KEY ,algorithm=ALGORITHM)

    return encoded_jwt  
    
def get_current_user(token:str=Depends(oauth2_scheme)) -> UserinDB:
    credintials_exceptions=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate the credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    
    try:
        payload=jwt.decode(token,SECRAT_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")

        if username is None:
            raise credintials_exceptions   

        token_data=TokenData(username=username)
    
    except JWTError:
        raise credintials_exceptions
    
    user=get_user(token_data.username)

    if user is None:
        raise credintials_exceptions
    
    return user

def get_current_active_user(current_user:UserinDB=Depends(get_current_user)) -> UserinDB:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="inactive user")
    
    return current_user