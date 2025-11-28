from sqlalchemy.ext import AsyncSession


class BaseRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
