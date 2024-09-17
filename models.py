from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    completed = Column(Boolean, default=False)

#In Simple Terms:

#This code defines the structure of a "to-do" item in the database. Each "to-do" has an id (a unique number), a name (the task or item name), and a completed status (whether it's done or not). This structure will be used to create a table in your database where all your "to-do" items will be stored.