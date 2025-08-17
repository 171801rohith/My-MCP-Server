from sqlalchemy import Column, String, Integer, DateTime, func
from database import Base


class MyNotes(Base):
    __tablename__ = "my_notes"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(String, nullable=False)
    date_time = Column(DateTime, default=func.now())
