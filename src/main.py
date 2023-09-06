import fastapi
import uvicorn
import logging


from fastapi.staticfiles import StaticFiles


from src.api.routers import all_routers

logger = logging.getLogger(__name__)


app = fastapi.FastAPI(title="CinemaManager")
app.mount("/static", StaticFiles(directory="src/static"), name="static")


for router in all_routers:
    app.include_router(router)

config = uvicorn.Config("src.main:app", port=5000, reload=True, log_level="info")
server = uvicorn.Server(config)
