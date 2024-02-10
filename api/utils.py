import io
import pandas as pd
from fastapi import UploadFile
from db.models import Route, Point
from db.dals import RouteDAL
from geopy.distance import geodesic


async def _load_point(db, lat_lng):
    async with db.begin():
        new_route = Route()
        db.add(new_route)
        await db.flush()
        for point_data in lat_lng:
            new_point = Point(lat=point_data['lat'], lng=point_data['lng'],
                              route_id=new_route.id)
            db.add(new_point)
    return new_route


async def read_uploaded_file(file: UploadFile):

    contents = await file.read()
    try:
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    except UnicodeDecodeError as e:
        print("Error decoding the file. Please ensure the file has the correct encoding.")
        raise e
    except Exception as e:
        print("An unknown error occurred while reading the file.")
        raise e
    try:
        lat_lng = df[['lat', 'lng']].to_dict('records')
    except KeyError as e:
        print("The file does not have the correct columns. Please ensure the file has the correct columns.")
        raise e
    return lat_lng


async def _get_route_by_id(route_id, session):
    async with session.begin():
        route_dal = RouteDAL(session)
        route = await route_dal.get_route_by_id(
            route_id=route_id,
        )
        if route is not None:
            return route


def calculate_distance(point1, point2):
    return geodesic((point1.lat, point1.lng), (point2.lat, point2.lng)).meters


def nearest_neighbor(points):
    start = points[0]
    route = [start]
    points.remove(start)
    while points:
        next_point = min(points,
                         key=lambda point: calculate_distance(start, point))
        route.append(next_point)
        points.remove(next_point)
        start = next_point
    return route
