from sqlalchemy import select
from src.repositories.base_repository import BaseRepository
from src.models import Zone


class ZoneRepository(BaseRepository):
    
    async def create(self, zone_data: dict):
        container = Zone(**zone_data)
        self.db.add(container)
        await self.db.commit()
        await self.db.refresh(container)
        return container

    async def get_all(self):
        result = await self.db.execute(select(Zone))
        return result.scalars().all()

    async def get_by_id(self, id: int):
        result = await self.db.execute(select(Zone).where(Zone.id == id))
        return result.scalar_one_or_none()

    async def update_load(self, zone: Zone, increment: int):
        zone.current_load += increment
        await self.db.commit()
