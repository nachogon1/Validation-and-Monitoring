#!/bin/sh
export IMAGE="validation-and-monitoring"
export CONTAINER="validation-and-monitoring"
if [ $(docker ps -a | grep ${CONTAINER} | wc -l) == 1 ]; then
    docker start ${CONTAINER}
    docker exec -it ${CONTAINER} bash
else
    docker image build -t ${IMAGE} .
    docker run -it -p 8000:8000 --network host -w /app --name ${CONTAINER} -v ${PWD}:/app ${IMAGE}  bash
fi