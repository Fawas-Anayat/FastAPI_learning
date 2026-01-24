from fastapi import FastAPI , status , HTTPException , Depends
from pydantic import BaseModel , EmailStr
from fastapi.responses import JSONResponse 
from sqlalchemy.orm import Session
from models import AuthorM , Post
from schemas import AuthorS , Posts
from db import get_db , Base , engine

app=FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/register")
def register_author(user : AuthorS, db:Session = Depends(get_db)):
    author_1 = AuthorM(name=user.name , email=user.email , password=user.password)
    db.add(author_1)
    db.commit()
    db.refresh

    return author_1


    

# @app.get("/authors")
# def get_all_authors():
#     if not db.authors:
#         raise HTTPException (status_code=404 , detail="no author found with this credentials")
#     auth_list= []
#     for user in db.authors.values():
#         auth_copy = user.copy()
#         auth_copy.pop("password",None)
#         auth_list.append(auth_copy)
#     return auth_list

# @app.post("/addPost")
# def add_post(post : Posts):


