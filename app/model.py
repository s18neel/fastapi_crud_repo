from sqlalchemy import Column, Integer, String
from config import Base

class Book(Base):
    __tablename__ = "book"

    id=Column(Integer,primary_key=True)
    title = Column(String[256])
    description = Column(String)



