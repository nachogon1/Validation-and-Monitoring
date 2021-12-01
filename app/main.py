from fastapi import FastAPI

from api.event import event_router

app = FastAPI()

app.include_router(event_router, prefix="/api/events")
