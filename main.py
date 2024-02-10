from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from api.handlers import routes_router

app = FastAPI(title='WelbeX', debug=True)

main_api_router = APIRouter()

main_api_router.include_router(routes_router, prefix="/api", tags=["api"])
app.include_router(main_api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
