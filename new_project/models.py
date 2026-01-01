import sqlalchemy
from database import metadata ,engine

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(100), unique=True, index=True)
)

# Create tables in DB
metadata.create_all(bind=engine)
