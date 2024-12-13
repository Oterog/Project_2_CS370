from sqlalchemy import Column, Integer, String
from turbogearsapp.model import DeclarativeBase

class TodoItem(DeclarativeBase):
    __tablename__ = 'todo_items'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
