# database.py
import databases
import sqlalchemy

# MySQL async URL
DATABASE_URL = "mysql+pymysql://fastapi_user:strongpassword@localhost/fastapi_db"

# Async database connection
database = databases.Database(DATABASE_URL)

# SQLAlchemy metadata for creating tables
metadata = sqlalchemy.MetaData()

# Engine for migrations / sync operations
engine = sqlalchemy.create_engine(DATABASE_URL.replace("+pymysql", ""))
