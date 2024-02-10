from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Route
from sqlalchemy.orm import joinedload


class RouteDAL:
    """Data Access Layer for operating route info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_route_by_id(self, route_id):
        result = await self.db_session.execute(select(
            Route).options(joinedload(Route.points)).where(
                Route.id == route_id))
        return result.scalars().first()
