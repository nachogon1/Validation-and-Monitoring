# Validation-and-Monitoring

Containerized python application for validating custom schema json events.

* [Objectives and Solutions](./solutions.md)

## Getting Started

### Requirements

* python3
* docker


### Installing

Clone this repo and go to the directory:

```
git clone https://github.com/nachogon1/Validation-and-Monitoring.git
cd Validation-and-Monitoring
```

Run this command to create a docker image and get inside its container (read below if you are using a mac):

```
bash develop.sh
```

From Mac. You might need to change `--network host` for `--network bridge` at `develop.sh`.

To delete the container and the image run this command:

```
bash destroy_develop.sh
```

After that, run this command to start the *app*. It will run on port 8000. All commands below are supposed to be run from the container.

From linux. Run to start the **app**.

```
uvicorn app.main:app
```

From Mac. Run to start the **app**.:

```
uvicorn app.main:app --host="0.0.0.0"
```

Once started, you can navigate to http://127.0.0.1:8000/docs or http://localhost/docs to view the Swagger documentation.

To run the scripts (from the container terminal):

For help, you can run:

```
events-tools --help 
```

Place your json events anywhere in the project and run:

For validating the events JSON.

```
events-tools validate-json --file $YOUR_PATH
```

For generating the reports of the JSON events.

```
events-tools generate-report --file $YOUR_PATH
```

The results will be logged in console and store in `/app/logs/scripts_log.log` and `/app/data/report_events.csv`. 

You may see something like:

```
2021-12-01 19:59:10.275635 INFO Event submission_success happens 1 times at 01/30/2018.
2021-12-01 19:59:10.275635 INFO Event fake_event_1 happens 2 times at 01/30/2018.
2021-12-01 19:59:10.275635 INFO Event registration_initiated happens 3 times at 02/03/2018.
```

```
event_name;concurrent_events;date
submission_success;01/30/2018;1
fake_event_1;01/30/2018;2
registration_initiated;02/03/2018;3
fake_event_2;02/03/2018;1
fake_event_3;04/01/2018;1
registration_initiated;02/20/2025;1
```

If you want to run my custom event json run:

```
export YOUR_PATH="/app/app/data/input.json"
```

### Testing

Run the following command:

```
pytest
```
