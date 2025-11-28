from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.database.connection import Base

class Container(Base):
    __tablename__ = "containers"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    arrival_time = Column(DateTime, default=func.now())
    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=True)
    zones = relationship("Zone", back_populates="container")
