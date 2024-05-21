from sqlalchemy import Boolean, Column, Integer, String
from database.database import Base

class Todo(Base):
    __tablename__ = 'todos'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(100))
    complete = Column('complete', Boolean, default=False)