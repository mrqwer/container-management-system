from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from enum import Enum


class ContainerStatus(str, Enum):
    NEW = "new"
    STORED = "stored"
    SHIPPED = "shipped"


class ContainerBase(BaseModel):
    number: str
    type: str
    status: ContainerStatus = ContainerStatus.NEW


class ContainerCreate(ContainerBase):
    pass


class ContainerRead(ContainerBase):
    id: int
    arrival_time: datetime
    zone_id: Optional[int]
    model_config = ConfigDict(from_attributes=True)
