from sqlalchemy import create_engine , ForeignKey 
from sqlalchemy.orm import declarative_base , Mapped , mapped_column , relationship 
from typing import List

db_url="sqlite:///database.db"

engine=create_engine(db_url,echo=True)    # manages all the connections between the SQL and the python and do inter-translate the code

Base=declarative_base()      # its a base class that provides the base from which all the classes of the database are inherited

class Basemodel(Base):
    __abstract__=True

    id:Mapped[int]=mapped_column(primary_key=True)


class Address(Basemodel):
    __tablename__="addresses"

    city:Mapped[str]=mapped_column(nullable=False)
    postal_address:Mapped[str]=mapped_column(nullable=True)
    user_id:Mapped[str]=mapped_column(ForeignKey("users.id"))
    user = relationship("User",back_populates="addresses")

class User(Basemodel):    # this python class represents a table in our database
    __tablename__ = "users"

    name:Mapped[str]=mapped_column(nullable=False)    # the none shows that the field is optional
    age:Mapped[int | None]=mapped_column()
    addresses:Mapped[list[str]]=relationship(Address,back_populates="user")

Base.metadata.create_all(engine)    # base.metadata collects all the definitions of the tables and then .creata_all do the connection with the database and then creates all the tables if they don't exist,,also it creates the database.db file if it don't exists

