from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.zone import ZoneService
from src.services.container import ContainerService
from src.schemas import ContainerCreate, ZoneCreate

class WarehouseService:
    """Domain Intersection Service"""
    def __init__(self, db: AsyncSession):
        self.container = ContainerService(db)
        self.zone = ZoneService(db)

    async def create_container(self, schema: ContainerCreate):
        return await self.container.create_container(schema)

    async def list_containers(self):
        return await self.container.list_containers()
    async def update_container_status(self, container_id: int, status: str):
        return await self.container.update_container_status(container_id, status)
    
    async def create_zone(self, schema: ZoneCreate):
        return await self.zone.create_zone(schema)

    async def list_zones(self):
        return await self.zone.list_zones()

    async def assign_container_to_zone(self, zone_id: int, container_id: int):
        zone = await self.zone.get_by_id(zone_id)
        container = await self.container.get_by_id(container_id)

        if not zone or not container:
            raise HTTPException(status_code=404, detail="Zone or Container not found")

        if zone.current_load >= zone.capacity:
            raise HTTPException(status_code=400, detail="Zone Overloaded")

        if container.zone_id:
             old_zone = await self.zone.get_by_id(container.zone_id)
             if old_zone:
                 await self.zone.update_load(old_zone, -1)

        container.zone_id = zone.id
        await self.container.repo.update(container) 
        await self.zone.update_load(zone, 1)

        return {"message": "assigned", "zone": zone.name, "container": container.number}
