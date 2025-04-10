from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.db import Base


class Tron(Base):
    __tablename__ = "tron"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    balance = Column(Integer)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())

class TronAddress(Base):
    __tablename__ = "tron_address"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    private_key = Column(String, index=True)