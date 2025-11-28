from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.zone import ZoneService
from src.services.container import ContainerService

from src.schemas.container import ContainerCreate

class WarehouseService:
    """Domain Intersection Service"""
    def __init__(self, db: AsyncSession):
        self.containers = ContainerService(db)
        self.zones = ZoneService(db)

    async def create_container(self, schema: ContainerCreate):
        return await self.containers.create_container(schema)

    async def list_containers(self):
        return await self.containers.list_containers()
    
    async def list_zones(self):
        return await self.zones.list_zones()

    async def assign_container_to_zone(self, zone_id: int, container_id: int):
        zone = await self.zones.get_by_id(zone_id)
        container = await self.containers.get_by_id(container_id)

        if not zone or not container:
            raise HTTPException(status_code=404, detail="Zone or Container not found")

        if zone.current_load >= zone.capacity:
            raise HTTPException(status_code=400, detail="Zone Overloaded")

        if container.zone_id:
             old_zone = await self.zones.get_by_id(container.zone_id)
             if old_zone:
                 await self.zones.update_load(old_zone, -1)

        container.zone_id = zone.id
        await self.containers.repo.update(container) 
        await self.zones.update_load(zone, 1)

        return {"message": "assigned", "zone": zone.name, "container": container.number}
