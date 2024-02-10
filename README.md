# WelbeX

Описание стека и запуск

Fastapi, Postgre, docker, python 3.10, asyncpg, pandas, alembic, SQLAlchemy and other...
.....
For begin and test project:

docker-compose -f docker-compose-local.yaml up -d
docker exec -it welbex-web-1 alembic upgrade heads

## Юнит-тесты 

Юнит-тест на проверку работы функции вычисления оптимального маршрута находитс в файле tests.py.

## Docker and docker-compose

Dockerfile и docker-compose-local.yaml находятся в основной директории.

## Опишите, каких endpoint-ов и методов не хватает в рамках REST API.
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
