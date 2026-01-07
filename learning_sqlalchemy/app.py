from models import User , engine
from sqlalchemy.orm import sessionmaker

# Session=sessionmaker(bind=engine)
# session=Session()
# user=User(id=101,name="usman",city="mansehra")
# Session.add(user)
# Session.commit()
# Session.close()

Session=sessionmaker(bind=engine)

# user_1=User(name="ahmad",city="islamabad")
# user_2=User(name="faizan",city="islamabad")
# user_3=User(name="maryam",city="karachi")
# user_4=User(name="meher",city="lahore")



# with Session() as session:
#     session.add_all([user_1,user_2,user_3,user_4])
#     session.commit()

session=Session()
users=session.query(User).all()

for user in users:
    print(F"id : {user.id} name: {user.name} city : {user.city}")
# user1=users[0]
# print(user1.id)
# print(user1.name)
# print(user1.city)