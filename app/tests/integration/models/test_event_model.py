import pytest
from pydantic import ValidationError


@pytest.mark.parametrize(
    "event, wanted_result",
    [
        (
            {
                "id": "FB16866D-AE4D-416F-8848-122B07DA42F5",
                "received_at": "2018-01-30 18:13:52.221000",
                "anonymous_id": "0A52CDC6-DDDC-4F7D-AA24-4447F6AF2689",
                "context_app_version": "1.2.3",
                "context_device_ad_tracking_enabled": True,
                "context_device_manufacturer": "Apple",
                "context_device_model": "iPhone8,4",
                "context_device_type": "android",
                "context_locale": "de-DE",
                "context_network_wifi": True,
                "context_os_name": "android",
                "context_timezone": "Europe/Berlin",
                "event": "submission_success",
                "event_text": "submissionSuccess",
                "original_timestamp": "2018-01-30T19:13:43.383+0100",
                "sent_at": "2018-01-30 18:13:51.000000",
                "timestamp": "2018-01-30 18:13:43.627000",
                "user_id": "18946",
                "context_network_carrier": "o2-de",
                "context_device_token": None,
                "context_traits_taxfix_language": "en-DE",
            },
            True,
        ),
        ({}, False),
    ],
)
def test_event_model(event, wanted_result):
    from models.event import Event

    try:
        Event.validate(event)
        assert wanted_result
    except ValidationError:
        assert not wanted_result
