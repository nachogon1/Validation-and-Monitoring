# Objectives and solutions

## Objective 1: Create a schema validator

### Description

1. Define a schema based on input.json file attached
2. Implement a schema validator
3. In case of errors (wrong data type, missing field, etc.), the validator should log them and
continue to next line of data

### Solution

For **objective 1**, The schema is defined under `/app/models/event.py`. I created the schema based on a provided input.json. In addition, I have added custom validators for the "context_version", the language code fields and the timezone field.

To validate the JSON events use the API or the CLI. Go to * [Installing](./README.md) for its functioning. The output will be either a response or a standard error log indicating which event does not fulfil the schema.

If you prefer to see the schema as a JSON you can get it from the API in swagger.

Notes:

In comparison to other schema validators, I used pydantic since it offers models with dot notation, has pythonic notation using type hinting notation; has more than 8k of stars in GitHub, and it is actively developed; is easily integrable with FastAPI which is a modern, async framework for building API's.

## Objective 2: Generate a report with the count of each 'event' in the file

### Description

1. Report should have these columns: name of event, date, count of events on that date
2. Assume that the input.json file cannot be loaded into memory all at once

### Solution

For **objective 2**, I created the `generate-report` script to generate the count of the concurrent events.

To get the reports the CLI. Go to * [Installing](./README.md) for its functioning.
The solution is logged out and added under `/app/logs/report_log.log` and written as a csv under `/app/data/report_log.log`.

Notes:

I use loguru for the logging and we will open files as an iterator since it won't fit in memory. In addition, we assume that the data is not sorted. 

The algorithm aggregates all the events by name and timestamp, for that purpose needs to keep a count of the events for each date. We could save some memory if we sorted the data with some big data algorithm like unix `sort` beforehand since we could treat the data by chunks.
Another way to save some memory would be eliminating useless fields beforehand.


## Miscellaneous

## Testing

The automatic tests helped to define the logic and for quality assurance. My tests could be more complete, but I made them as a proof of concept.