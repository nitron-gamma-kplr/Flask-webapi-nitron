from sqlalchemy import create_engine, text
import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_login import UserMixin
import flask_login

url="postgresql+psycopg2://leiceswo:uToAdZce6aBxkF62X-EfwXudPDRM0F2U@horton.db.elephantsql.com/leiceswo"
engine=create_engine(url)
Session = sessionmaker(bind = engine)
session=Session()


Base = declarative_base()


class IncomeExpenses(Base):
    __tablename__ = 'api_sold'
   
    id = Column(Integer, primary_key = True)
    type = Column(String(30), default="income")
   
    def __repr__(self):
        return f"user {self.id}" + f"type {self.type}"

class User(Base,UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    email = Column(VARCHAR, unique=True, nullable=False)
    password = Column(VARCHAR, nullable=False)
    name = Column(VARCHAR, nullable=False)
   
    def __repr__(self):
        return f"id : {self.id}" + f"email : {self.email}" + f"password : {self.id}" + f"name : {self.email}"

'''
Base.metadata.create_all(engine)

user = User(
    id=1,
    email="admin@example.com",
    password="Please don't set passwords like this",
    name="Todd")

session.add(user)  # Add the user
session.commit()  # Commit the change
'''


