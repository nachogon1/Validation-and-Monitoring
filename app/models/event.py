import re
from datetime import datetime
from typing import Optional
from langcodes import tag_is_valid
import pytz

from pydantic import BaseModel, validator


class Event(BaseModel):
    id: str
    received_at: datetime
    anonymous_id: str
    context_app_version: str = "latest"
    context_device_ad_tracking_enabled: bool = False
    context_device_manufacturer: str
    context_device_model: str
    context_device_type: str
    context_locale: str = "de-DE"
    context_network_wifi: bool
    context_os_name: str
    context_timezone: Optional[str]
    event: str
    event_text: str
    original_timestamp: datetime
    sent_at: datetime
    timestamp: datetime
    user_id: Optional[int]
    context_network_carrier: str
    context_device_token: str = None
    context_traits_taxfix_language: str = "de-DE"

    @validator("context_app_version")
    def check_context_app_version(cls, v):
        version_rule = re.compile("^[0-9]+\.[0-9]+\.[0-9]+$")
        if version_rule.match(v) or v == "latest":
            return v
        else:
            raise ValueError(f"{v} is not a valid context app version.")

    @validator("context_locale", "context_traits_taxfix_language")
    def check_langcodes(cls, v):
        if tag_is_valid(v):
            return v
        else:
            raise ValueError(f"{v} is not a language code.")

    @validator("context_timezone")
    def check_timezones(cls, v):
        if v in pytz.all_timezones:
            return v
        else:
            raise ValueError(f"{v} is not a valid timezone.")
