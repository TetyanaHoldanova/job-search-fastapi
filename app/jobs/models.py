from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, DateTime
import datetime

from ..db import Base



class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String)
    description = Column(String)
    salary_from = Column(Integer)
    salary_to = Column(Integer)
    is_active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
