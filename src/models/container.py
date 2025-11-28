from sqlalchemy import Column, Integer, String, ForeignKey, Datetime, func
from sqlalchemy.orm import relationship


class Container(Base):
    __tablename__ = "containers"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    arrival_time = Column(Datetime, default=func.now())
    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=True)
    zone = relationship("Zone", back_populates="containers")
