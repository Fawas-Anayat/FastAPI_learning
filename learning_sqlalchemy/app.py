from models import User , engine
from sqlalchemy.orm import sessionmaker
import random
from sqlalchemy import func

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

# session=Session()
# users=session.query(User).filter_by(id=102).first()

# for user in users:
    # user.name="abuzar"
# session.delete(users)
# session.commit()
    # print(F"id : {user.id} name: {user.name} city : {user.city}")
# user1=users[0]
# print(user1.id)
# print(user1.name)
# print(user1.city)

session=Session()

# usernames=["khan","faizan","farhan","shahzaib","zeb khan"]
# cities=["mansehra","murre","nathiagali","balakot","naran"]

# for x in range(5):
#     user=User(name=random.choice(usernames),city=random.choice(cities))
#     session.add(user)

# session.commit()

# users=session.query(User).filter(User.city=="islamabad").all()   # filter_by uses only the equality for the filtering of the data while the filter uses also the comparison operetors , <=,> etc and its more efficient to use the simple filter more often

# in the process of  the filterng we can use the or_ , not_ and the and_ methods to manipulate the data accordingly
# users=session.query(User).where(User.id==103).all()

users=session.query(User.city,func.count(User.id).label("count")).group_by(User.city).all()

# print(users)

for u in users:
    print(f"city:{u.city} count {u.count}")
