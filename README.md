# WelbeX

## Stack
Fastapi, Postgre, docker, python 3.10, asyncpg, pandas, alembic, SQLAlchemy and other(check requirements.txt)
![python version](https://img.shields.io/badge/Python-3.10-yellow)
![fastapi version](https://img.shields.io/badge/fastapi-0.109.2-blue)
![postgresql version](https://img.shields.io/badge/postgresql-latest-green)
![docker version](https://img.shields.io/badge/Docker-blue)

..... 
## For begin and test project:
```
git clone git@github.com:iamlilze/WelbeX.git
```
```
docker-compose -f docker-compose-local.yaml up -d
```
```
docker exec -it welbex-web-1 alembic upgrade heads
```
## Examples of requests

1. POST /api/routes
Request:
```
POST /api/routes HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="route.csv"
Content-Type: text/csv

(lat,lng)
40.7128,74.0060
51.5074,0.1278
48.8566,2.3522
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```
Response:
```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "points": [
    {"lat": 40.7128, "lng": 74.0060},
    {"lat": 51.5074, "lng": 0.1278},
    {"lat": 48.8566, "lng": 2.3522}
  ]
}
```
2. GET /api/routes/{id}
Request:
```
GET /api/routes/1 HTTP/1.1
```
Response:
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "New Route",
  "points": [
    {"lat": 40.7128, "lng": 74.0060},
    {"lat": 48.8566, "lng": 2.3522},
    {"lat": 51.5074, "lng": 0.1278}
  ]
}
```
### Юнит-тесты 

Юнит-тест на проверку работы функции вычисления оптимального маршрута находитс в файле tests.py.

### Docker and docker-compose

Dockerfile и docker-compose-local.yaml находятся в основной директории.

### Опишите, каких endpoint-ов и методов не хватает в рамках REST API.
В рамках REST API для работы с маршрутами, в дополнение к уже реализованным endpoint'ам, могут быть полезны следующие:

GET /api/routes - получение списка всех маршрутов.
Этот endpoint может поддерживать различные параметры для фильтрации, сортировки и пагинации.

PUT /api/routes/{id} - обновление маршрута по id.
Этот endpoint может использоваться для обновления существующего маршрута.

DELETE /api/routes/{id} - удаление маршрута по id.
Этот endpoint может использоваться для удаления существующего маршрута.

POST /api/routes/{id}/points - добавление точки к маршруту.
Этот endpoint может использоваться для добавления новой точки к существующему маршруту.

GET /api/routes/{id}/points - получение списка всех точек маршрута.
Этот endpoint может поддерживать различные параметры для фильтрации, сортировки и пагинации.

PUT /api/routes/{id}/points/{point_id} - обновление точки маршрута по id.
Этот endpoint может использоваться для обновления существующей точки маршрута.

DELETE /api/routes/{id}/points/{point_id} - удаление точки маршрута по id.
Этот endpoint может использоваться для удаления существующей точки маршрута.

GET /api/routes/{id}/optimize - оптимизация маршрута.
Этот endpoint может использоваться для запуска процесса оптимизации маршрута.
