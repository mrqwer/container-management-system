from src.services.base_service import BaseService
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories import ZoneRepository

class ZoneService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(db)
        self.repo = ZoneRepository(db)

    async def create_zone(self, schema):
        return await self.repo.create(schema.model_dump())
    
    async def list_zones(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, zone_id: int):
        return await self.repo.get_by_id(zone_id)
        
    async def update_load(self, zone, increment: int):
        return await self.repo.update_load(zone, increment)
