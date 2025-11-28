from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ContainerBase(BaseModel):
    number: str
    type: str
    status: str = "new"


class ContainerCreate(ContainerBase):
    pass


class ContainerRead(ContainerBase):
    id: int
    arrival_time: datetime
    zone_id: Optional[int]
    model_config = ConfigDict(from_attributes=True)
