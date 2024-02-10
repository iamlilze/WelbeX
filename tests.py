import pytest
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from unittest.mock import AsyncMock, MagicMock
from api.utils import _load_point, read_uploaded_file
from api.utils import calculate_distance, nearest_neighbor
from geopy.distance import geodesic
from collections import namedtuple


@pytest.mark.asyncio
async def test_load_point():
    db = AsyncMock(spec=AsyncSession)
    lat_lng = [{'lat': 1.0, 'lng': 1.0}, {'lat': 2.0, 'lng': 2.0}]
    new_route = await _load_point(db, lat_lng)
    assert new_route is not None
    assert db.begin.called
    assert db.add.called
    assert db.flush.called


@pytest.mark.asyncio
async def test_read_uploaded_file():
    data = 'lat,lng\n1.0,1.0\n2.0,2.0\n'
    file = MagicMock(spec=UploadFile)
    file.read = AsyncMock(return_value=data.encode('utf-8'))
    lat_lng = await read_uploaded_file(file)
    assert lat_lng == [{'lat': 1.0, 'lng': 1.0}, {'lat': 2.0, 'lng': 2.0}]
    file.read.assert_awaited()


@pytest.mark.asyncio
async def test_read_uploaded_file_with_invalid_data():
    data = 'invalid data'
    file = MagicMock(spec=UploadFile)
    file.read = AsyncMock(return_value=data.encode('utf-8'))
    with pytest.raises(Exception):
        await read_uploaded_file(file)


Point = namedtuple('Point', ['lat', 'lng'])


def test_calculate_distance():
    point1 = Point(1.0, 1.0)
    point2 = Point(2.0, 2.0)
    expected_distance = geodesic((1.0, 1.0), (2.0, 2.0)).meters
    assert calculate_distance(point1, point2) == expected_distance


@pytest.mark.parametrize("points,expected_route", [
    ([Point(1.0, 1.0), Point(2.0, 2.0), Point(3.0, 3.0)],
     [Point(1.0, 1.0), Point(2.0, 2.0), Point(3.0, 3.0)]),
    ([Point(40.7128, 74.0060), Point(51.5074, 0.1278), Point(48.8566, 2.3522)],
     [Point(40.7128, 74.0060), Point(48.8566, 2.3522), Point(51.5074, 0.1278)]),
    ([Point(51.5074, -0.1278), Point(34.0522, -118.2437), Point(-33.8688, 151.2093)],
     [Point(51.5074, -0.1278), Point(34.0522, -118.2437), Point(-33.8688, 151.2093)])
])
def test_nearest_neighbor(points, expected_route):
    assert nearest_neighbor(points) == expected_route
