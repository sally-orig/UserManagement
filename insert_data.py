# insert_data.py
from UserManagement.db import SessionLocal
from UserManagement.models import User

# Create a session to interact with the database
session = SessionLocal()

# Insert new users manually
try:
    # Example of adding new users
    user1 = User(email="test@email.com", age=28, date_of_birth="1997-03-10")
    user2 = User(email="t@email.com", age=18, date_of_birth="2007-03-10")
    user3 = User(email="est@email.com", age=32, date_of_birth="1993-01-24")
    user4 = User(email="samp@test.com", age=33, date_of_birth="1994-10-04")
    user5 = User(email="sample@email.com", age=26, date_of_birth="1999-11-08")
    user6 = User(email="sample@test.com", age=25, date_of_birth="2000-07-08")
    user7 = User(email="hotmail@email.com", age=30, date_of_birth="1995-03-28")
    user8 = User(email="mail@email.com", age=30, date_of_birth="1995-11-11")
    user9 = User(email="my@gmail.com", age=24, date_of_birth="2001-04-04")
    user10 = User(email="opcors@email.com", age=14, date_of_birth="2011-12-04")

    # Add the users to the session
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.add(user5)
    session.add(user6)
    session.add(user7)
    session.add(user8)
    session.add(user9)
    session.add(user10)

    # Commit the transaction
    session.commit()
    print("Data inserted successfully!")

except Exception as e:
    print(f"Error inserting data: {e}")
    session.rollback()

finally:
    # Close the session
    session.close()
