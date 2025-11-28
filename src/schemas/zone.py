from pydantic import BaseModel, ConfigDict


class ZoneBase(BaseModel):
    name: str
    capacity: int
    zone_type: str


class ZoneCreate(ZoneBase):
    pass


class ZoneRead(ZoneBase):
    id: int
    current_load: int
    model_config = ConfigDict(from_attributes=True)
