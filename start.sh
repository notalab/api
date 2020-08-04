#/bin/bash
docker run --name nota \
    -e APPLICATION_POSTGRES_HOST='127.0.0.1' \
    -e APPLICATION_POSTGRES_USER='docker' \
    -e APPLICATION_POSTGRES_PW='docker' \
    -e APPLICATION_POSTGRES_PORT='32768' \
    -e APPLICATION_POSTGRES_DB='docker' \
    -e ENVIRONMENT='dev' \
    -d -p 8000:5000 nota:latest
