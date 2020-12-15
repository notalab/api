#/bin/bash
docker build -t nota:latest .
    docker stop nota && docker rm nota
    docker run --name nota \
    -e APPLICATION_POSTGRES_HOST=$APPLICATION_POSTGRES_HOST \
    -e APPLICATION_POSTGRES_USER=$APPLICATION_POSTGRES_USER \
    -e APPLICATION_POSTGRES_PW=$APPLICATION_POSTGRES_PW \
    -e APPLICATION_POSTGRES_PORT=$APPLICATION_POSTGRES_PORT \
    -e APPLICATION_POSTGRES_DB=$APPLICATION_POSTGRES_DB \
    -e ENVIRONMENT=dev \
    -d -p 8000:5000 nota:latest
    git status
