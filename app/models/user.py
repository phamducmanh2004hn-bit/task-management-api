from app.db.base import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    tasks = relationship("Task", back_populates="user") 