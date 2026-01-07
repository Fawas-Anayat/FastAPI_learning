from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base , Mapped , mapped_column

db_url="sqlite:///database.db"

engine=create_engine(db_url)    # manages all the connections between the SQL and the python and do inter-translate the code

Base=declarative_base()      # its a base class that provides the base from which all the classes of the database are inherited

class User(Base):    # this python class represents a table in our database
    __tablename__ = "users"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str | None]=mapped_column()    # the none shows that the field is optional
    city:Mapped[str | None]=mapped_column()

Base.metadata.create_all(engine)    # base.metadata collects all the definitions of the tables and then .creata_all do the connection with the database and then creates all the tables if they don't exist,,also it creates the database.db file if it don't exists

