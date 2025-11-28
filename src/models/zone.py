from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Zone(Base):
    __tablename__ = "zone"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    current_load = Column(Integer, default=0, nullable=False)
    zone_type = Column(String, nullable=False)

    containers = relationship("Container", back_populates="zone")
