from sqlalchemy import Column, Integer, String
from database import BaseModel

class Info(Base):
    __tablename__ = "info"

    first_name = Column(String, primary_key = True, index=True)
    last_name = Column(String)
    birthday = Column(String)
    file = Column(String)