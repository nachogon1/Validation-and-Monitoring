import json

from models.event import Event


def insert_report_data(line, count_dict):
    event = Event(**json.loads(line))
    event_date = event.original_timestamp.date()
    if count_dict.get(event_date):
        daily_count = count_dict[event_date]
        if event.event in daily_count:
            daily_count[event.event] += 1
        else:
            daily_count[event.event] = 1
    else:
        daily_count = {event.event: 1}
    count_dict[event_date] = daily_count
    return count_dict
