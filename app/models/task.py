from app.db.base import Base
from sqlalchemy import Column,Integer,String,Text,ForeignKey
from sqlalchemy.orm import relationship  
class Task(Base):
    __tablename__ = "task"
    id = Column(Integer,primary_key = True)
    title = Column(String)
    description = Column(Text)
    status = Column(String)
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("User", back_populates="tasks")