# This is used by the sqlalchemy uses to be able to create the tables needed in mysql database

from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)      #index=True implies it will improve mysql performance when search by id
    username = Column(String, unique=True,nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)