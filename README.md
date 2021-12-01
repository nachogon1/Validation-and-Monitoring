# Validation-and-Monitoring
Containerized python application for validating custom schema json events.


# How to use

From your terminal:

```
git clone https://github.com/nachogon1/Validation-and-Monitoring.git
cd Validation-and-Monitoring
```

Run to create an image and get inside the container:
```
bash develop.sh
```


All the commands below are supposed to be run from the container.

From linux. Run to start the **app**.
```
uvicorn app.main:app
```

From Mac. You might need to change `--network host` for `--network bridge` at develop.sh and run:

```
uvicorn app.main:app --host="0.0.0.0"
```


Then, you can open **swagger** in your browser under http:127.0.0.1:8000/docs, 
where you can validate JSON events.


To run the **tests**: 

```
pytest
```

To run the scripts:
For help you can run:

```
events-tools --help 
```


Place your json events under anywhere in the project and run:

```
events-tools validate-json --file $YOUR_PATH
```


```
events-tools generate-report --file $YOUR_PATH
```


If you want to run my custom event json run:

```
export YOUR_PATH="/app/app/data/input.json"
```

The results will be written under `/app/app/data/report_log_1.log` .

To delete the container run

```
bash destroy_develop.sh
```


# Objectives
Objective 1: Create a schema validator
1. Define a schema based on input.json file attached
2. Implement a schema validator
3. In case of errors (wrong data type, missing field, etc.), the validator should log them and
continue to next line of data
Objective 2: Generate a report with count of each “event” in the file
1. Report should have these columns: name of event, date, count of events on that date
2. Assume that the input.json file cannot be loaded into memory all at once

# My Solution

For **objective 1**, The schema is defined under `/app/models/event.py`. I created the schema based on a provided input.json.
In addition, I have added custom validators for the "context_version", the language code fields and the timezone field.

To validate the json events use the API or the CLI. Go to "How to use" for its functioning. The output will be either
a response or a standard error log indicating which event does not fulfill the schema.

If you prefer to see the schema as a json you can get it from the api in swagger.

Notes:

In comparison to other schema validators, I used pydantic since it offers models with dot notation,
has pythonic notation using type hinting notation; has more than 8k of stars in github
and it is actively developed; is easily integrable with FastAPI which is a modern, async framework for building API's.



For **objective 2**, I created the `generate-report` script to generate the count of the co-occurrent events.
To get the reports the CLI. Go to "How to use" for its functioning.
The solution is logged out and added under `/app/logs/report_log_1.log`.

Notes:

I will use loguru for the logging and we will open files as an interator since it won't fit in memory.
To get the date agregation of each event we assume that the events are not necessarily sorted.
For the algorithm to use we have to possibilities, the first one consists in sorting the events beforehand by some efficient
algorithm like unix sort, iterate over events the storing the ids, and log them out at the beginning of the next chunk.
This approach add some complexity time overhead O(n*log(n)), but we only need to save the ids from one chunk.
The second possibilty is to iterate over all the unsorted events, save all the ids under its respective timestamp and
at the end of the file, log them all out. To get into situation, a python occupies 1 byte, therefore if we had a normal RAM of 16gb, we could
do reports of approximately 44 millions of events without worrying about memory. To properly choose between one or 
another I would need to have more information like the cloud provider and how it is intended to be use.

I will procceed with the second possibility since I am not sure of the format of the input data.
I find missleading that the input.json is not a real JSON.

# Testing
The autmatic tests help defining the business logic and for quality assurance. My tests could be more complete,
but I made them as a proof of concept.






For maximum efficiency we could use some technics to remove useless json fields trading some complexity time for
memory since we only need the name and timestamp.