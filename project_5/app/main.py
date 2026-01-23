from fastapi import FastAPI , status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI()

@app.get("/users/{user_id}")
def user_detail(user_id:int):
    if user_id == 101:
        content={"user_id":user_id,"user_name":"usman"}
        header={"Cache-Control":"public,max_age=3600"}
        return JSONResponse (content=content , status_code=status.HTTP_200_OK, headers=header)
    
@app.get("/users/{user_id}/{city}", response_class=JSONResponse)
def get_user_by_user_id__and_city(user_id:int,city:str) -> JSONResponse:
    content = {"name":"khan","city":city , "user_id":user_id}
    header = {"response type":"json", "made by ": "fastapi web application" , "Cached-Control":"public ,max_age=3600"}
    return JSONResponse (content=content , headers=header , status_code=status.HTTP_200_OK)

# this is the wrong aproach , for the post requests , always use the proper pydanctic model schemas
# @app.post("/users/create", response_class=JSONResponse)
# def create_user(name:str , user_id:int , city : str = "Masnehra") -> JSONResponse :
#     content = { "name" : name , "user_id":user_id , "city":city}
#     header = {"type":"jsonResponse",}
#     return JSONResponse (headers=header , content= content , status_code= status.HTTP_201_CREATED)

class UserCreate(BaseModel):
    id :int 
    name:str
    city : str = "Mansehra"

@app.post("/users/create")
def create_user(user : UserCreate):
    content = {
        "id" : user.id,
        "name" : user.name ,
        "city" : user.city ,
        "message" : "user created successfully"
    }
    header = {
        "Cache-Control":"no-cache",
    }
    return JSONResponse (
        headers= header ,
        content=content ,
        status_code=status.HTTP_201_CREATED
    )