#!/bin/bash
docker build -t kdop/frontend-app:0.0.1 .
#docker push kdop/frontend-app:0.0.1
docker run --rm -p 5000:5000 --name=frontend-app kdop/frontend-app:0.0.1