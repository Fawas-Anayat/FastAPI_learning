from pydantic import BaseModel , EmailStr , Field

class AuthorS(BaseModel):
    name : str
    email : EmailStr
    password : str = Field(... , min_length=8)
    posts_count : int

class Posts(BaseModel):
    author_id : int
    post_content : str = Field (... , min_length=5 , max_length= 500)

