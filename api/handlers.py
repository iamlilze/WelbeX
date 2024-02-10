from fastapi import APIRouter
from fastapi import File, UploadFile
from .schemas import RouteBase
from db.session import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .utils import (_load_point, read_uploaded_file,
                    _get_route_by_id, nearest_neighbor)


routes_router = APIRouter()


@routes_router.post("/routes", response_model=RouteBase)
async def create_route(file: UploadFile = File(...),
                       db: AsyncSession = Depends(get_db),
                       ):
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Please upload a CSV file.")
    lat_lng = await read_uploaded_file(file)
    new_route = await _load_point(db, lat_lng)

    return {"id": new_route.id, "points": lat_lng}


@routes_router.get("/routes/{route_id}", response_model=RouteBase)
async def get_route_by_id(
    route_id: int,
    db: AsyncSession = Depends(get_db),
) -> RouteBase:
    route = await _get_route_by_id(route_id, db)
    if route is None:
        raise HTTPException(
            status_code=404, detail=f"Route with id {route_id} not found."
        )
    points = nearest_neighbor(route.points)

    return {"id": route.id, "points": points}
