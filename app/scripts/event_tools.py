import datetime
import json

import click
from core.config import LOG_PATH
from loguru import logger
from models.event import Event
from pydantic import ValidationError

from core.config import REPORT_EVENTS_PATH


@click.group()
@click.pass_context
def main(ctx):
    """Script cli."""
    logger.add(
        f"{LOG_PATH}",
        format="{extra[executed]} {level} {message}",
    )
    ctx.obj = logger


@main.command()
@click.option("--file", help="Generate Report")
def validate_json(file):
    """Validate the events from the events of a file"""
    with open(file) as file:  # Open file as an iterator to save memory.
        for i, line in enumerate(file):
            try:
                Event(**json.loads(line))
            except ValidationError as e:
                logger.error(
                    f"Validation error at event {i + 1} with errors {e.json()}"
                )


@main.command()
@click.option("--file", help="Generate Report")
@click.pass_context
def generate_report(ctx, file):
    """Create report from events file with name of event, date, count of events"""
    logger = ctx.obj
    count_dict = {}
    script_runtime = datetime.datetime.utcnow()
    # Calculate the event occurence.
    with open(file) as file:  # Open file as an iterator to save memory.
        for line in file:
            try:
                event = Event(**json.loads(line))
                if count_dict.get(event.original_timestamp.date()):
                    daily_count = count_dict[event.original_timestamp.date()]
                    daily_count["events"].add(event.event)
                    daily_count["counter"] += 1

                else:
                    daily_count = {"events": set([event.event]), "counter": 1}

                count_dict[event.original_timestamp.date()] = daily_count
            except ValidationError:
                continue
        # Report to csv and logs.
        with open(REPORT_EVENTS_PATH, "w") as report:
            report.write(f"event_name;concurrent_events;date\n")
            for j, date in enumerate(count_dict):
                for event in count_dict[date]["events"]:
                    logger.bind(executed=script_runtime, name=id).info(
                        f"Event {event} cooccur with {count_dict[date]['counter']} events at {date.strftime('%m/%d/%Y')}."
                    )
                    report.write(f"{event};{count_dict[date]['counter']};{date.strftime('%m/%d/%Y')}\n")

