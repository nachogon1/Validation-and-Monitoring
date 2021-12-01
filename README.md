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

Run this command to create a docker image and get inside its container:

```
bash develop.sh
```

To delete the container and the image run this command:

```
bash destroy_develop.sh
```


After that, run this command to start the *app*. It will run on port 8000. All commands below are supposed to be run from the container.

From linux. Run to start the **app**.
```
uvicorn app.main:app
```

From Mac. You might need to change `--network host` for `--network bridge` at develop.sh and run:

```
uvicorn app.main:app --host="0.0.0.0"
```

Once started, you can navigate to http:127.0.0.1:8000/docs or http://localhost/docs to view the Swagger documentation.

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




The results will be written under `/app/app/data/report_log.log` .


### Testing

Run the following command:

```
pytest
```
