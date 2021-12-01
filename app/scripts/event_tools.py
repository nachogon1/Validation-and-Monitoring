import datetime
import json

import click
from pydantic import ValidationError

from models.event import Event

from loguru import logger

import os

from core.config import LOG_PATH


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
    with open(file) as file:  # Open file as an iterator to save memory.
        for line in file:
            try:
                event = Event(**json.loads(line))
                if count_dict.get(event.original_timestamp.date()):
                    count_dict[event.original_timestamp.date()] += [event.id]
                else:
                    count_dict[event.original_timestamp.date()] = [event.id]
            except ValidationError:
                continue
        for date in count_dict:
            for id in count_dict[date]:
                logger.bind(executed=script_runtime, name=id).info(
                    f"Event {id} cooccur with {len(count_dict[date])} events at {date.strftime('%m/%d/%Y')}."
                )
