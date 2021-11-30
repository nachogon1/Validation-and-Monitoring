# Validation-and-Monitoring
Example of schema validation and error monitoring


# Objectives
Objective 1: Create a schema validator
1. Define a schema based on input.json file attached
2. Implement a schema validator
3. In case of errors (wrong data type, missing field, etc.), the validator should log them and
continue to next line of data
Objective 2: Generate a report with count of each “event” in the file
1. Report should have these columns: name of event, date, count of events on that date
2. Assume that the input.json file cannot be loaded into memory all at once


For objective 1, in comparison to other schema validators, I will use pydantic since it offers models with dot notation,
has pythonic notation using type hintinng notation, has more than 8k of stars in github,
and it is actively developed, is easily integrable with FastAPI which is a modern, async framework for building API's.

For objective 2, I will use loguru and we will open files as an interator.
