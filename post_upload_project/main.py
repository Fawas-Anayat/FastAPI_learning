from fastapi import FastAPI , status , HTTPException , Depends
from pydantic import BaseModel , EmailStr
from fastapi.responses import JSONResponse 
from sqlalchemy.orm import Session
from models import AuthorM , Post
from schemas import AuthorS , Posts ,  Login
from db import get_db , Base , engine
from auth import hash_password , verify_password , verify_token , create_access_token , authinticate_user ,  get_current_user , create_tokens
from fastapi.security import OAuth2PasswordRequestForm 

app=FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/register")
def register_author(user : AuthorS, db:Session = Depends(get_db)):
    hashed_password=hash_password(user.password)
    author_1 = AuthorM(name=user.name , email=user.email , password=hashed_password)
    db.add(author_1)
    db.commit()
    db.refresh(author_1)

    return {
        "id": author_1.id,
        "name": author_1.name,
        "email": author_1.email,
        "message": "Author registered successfully"
    }

    


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user=authinticate_user(form_data.password, form_data.username, db)

    if user is False:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid username or password"
        )
    
    tokens = create_tokens(user,db)
    return {
        "access_token" : tokens["access_token"] ,
        "refresh-token" : tokens["refresh_token"] ,
        "token_type" : tokens["token_type"] ,
        "user" : {
            "id" : user.id ,
            "name" : user.name ,
            "email": user.email
        }
    }


@app.post('/uploadPost')
def upload_post(post : Posts ,user : AuthorM = Depends(get_current_user) , db : Session = Depends(get_db)):
    # user = authinticate_user(user.password, user.email, db)
    
    # if user is False:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="you are unauthorised to perform this action")
    new_post = Post(content=post.post_content , author = user)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return{
        "message" : "post uploaded successfully"
    }
    


