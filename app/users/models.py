from sqlalchemy import Column, Integer, String, Boolean, DateTime
import datetime

from ..db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    email = Column(String, primary_key=True, unique=True)
    name = Column(String)
    hashed_password = Column(String)
    is_company = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)