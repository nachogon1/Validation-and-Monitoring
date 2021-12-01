#!/bin/sh

export PROJECT_NAME=validation-and-monitoring
docker stop $PROJECT_NAME
docker rm $PROJECT_NAME
docker rmi $PROJECT_NAME