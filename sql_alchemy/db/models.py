# This is used by the sqlalchemy to create the tables needed in the database

from sqlalchemy import Column, Integer, String
from .database_conn import Base


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)  #index=True implies it will improve mysql performance when search by id
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    # is_active = Column(Boolean, default=True)
