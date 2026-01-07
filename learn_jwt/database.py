from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

# FAKE USERS DATABASE
# Key: username, Value: user data
fake_users_db = {
    "usman": {
        "user_id": 101,
        "username": "usman",
        "email": "usman@example.com",
        "hashed_password": pwd_context.hash("secret123"),  # Password: secret123
        "disabled": False
    },
    "alice": {
        "user_id": 102,
        "username": "alice",
        "email": "alice@example.com",
        "hashed_password": pwd_context.hash("alicepass"),  # Password: alicepass
        "disabled": False
     },
}