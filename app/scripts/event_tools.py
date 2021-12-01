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
        level="INFO"
    )
    ctx.obj = logger


@main.command()
@click.option("--file", help="Generate Report")
def validate_json(file):
    """Validate the events from the events of a file."""
    script_runtime = datetime.datetime.utcnow()
    with open(file) as file:  # Open file as an iterator to save memory.
        for i, line in enumerate(file):
            try:
                Event(**json.loads(line))
            except ValidationError as e:
                logger.bind(executed=script_runtime).error(
                    f"Validation error at event index { i } with errors {e.json()}"
                )


@main.command()
@click.option("--file", help="Generate Report")
@click.pass_context
def generate_report(ctx, file):
    """Create report from events file with name of event, date, count of events."""
    logger = ctx.obj
    count_dict = {}
    script_runtime = datetime.datetime.utcnow()
    # Calculate the event occurrence by date.
    with open(file) as file:  # Open file as an iterator to save memory.
        for line in file:
            try:
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
            except ValidationError:
                # Skip wrong data
                continue
        # Report to csv and logs.
        with open(REPORT_EVENTS_PATH, "w") as report:
            report.write(f"event_name;concurrent_events;date\n")
            for j, date in enumerate(count_dict):
                for event in count_dict[date]:
                    logger.bind(executed=script_runtime).info(
                        f"Event {event} happens {count_dict[date][event]} times at {date.strftime('%m/%d/%Y')}."
                    )
                    report.write(f"{event};{date.strftime('%m/%d/%Y')};{count_dict[date][event]}\n")

