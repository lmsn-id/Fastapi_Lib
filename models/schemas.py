from sqlalchemy import Column, String, Text, JSON, TIMESTAMP, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Test(Base):
    __tablename__ = "test"
    
    id = Column(String(20), primary_key=True)