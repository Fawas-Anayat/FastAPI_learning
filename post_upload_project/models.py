from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import ForeignKey
from typing import List
from db import Base

""" UNDERSTANDING THE RELATIONSHIPS"""



class AuthorM(Base):

    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(nullable=False, unique=True)
    email : Mapped[str] = mapped_column()
    password : Mapped[str] = mapped_column()
    posts_count :Mapped[int] = mapped_column(default=0 , server_default='0')

    posts = relationship("Post",back_populates="author")    # if don't put uselist=false then its one to many relationship

class Post(Base):

    __tablename__ = "posts"

    id : Mapped[int] = mapped_column(primary_key=True)
    author_id : Mapped[int] = mapped_column(ForeignKey("authors.id"))
    content : Mapped[str] = mapped_column()

    author = relationship("AuthorM" ,back_populates="posts")

