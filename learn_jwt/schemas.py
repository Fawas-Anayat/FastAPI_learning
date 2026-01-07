from pydantic import BaseModel
from typing import Optional

class Create_user(BaseModel):   # this is the class for when first time user registers on the website
    username:str
    email:str
    password:str   # the password will be hashed before storing in the database

class User(BaseModel):    
    user_id:int
    username:str
    email:str

class UserinDB(User):          # this is the class for saving the user in the database as it inheriting all the data from the user class and also has the hashed password
    hashed_password:str
    disabled:bool

class TokenData(BaseModel):
    username:Optional[str]