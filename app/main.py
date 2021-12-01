from api.event import event_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(event_router, prefix="/api/events", tags=["Events"])
