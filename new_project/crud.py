from models import users
from database import database

async def create_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    user_id = await database.execute(query)
    return {"id": user_id, "name": name, "email": email}

async def get_users():
    query = users.select()
    return await database.fetch_all(query)
