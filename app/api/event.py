from typing import List

from fastapi import APIRouter
from models.event import Event

event_router = APIRouter()


@event_router.post("/checker")
def validate_event_schema(events: List[Event]):
    return events


@event_router.get("/schema")
def get_json_schema() -> str:
    return Event.schema_json(indent=2)
