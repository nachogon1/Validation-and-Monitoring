from typing import List

from fastapi import APIRouter
from models.event import Event

event_router = APIRouter()


@event_router.post("/checker")
def validate_event_schema(events: List[Event]):
    return events
