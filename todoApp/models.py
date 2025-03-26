from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)

