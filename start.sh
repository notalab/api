#/bin/bash
docker run --name nota -d -p 8000:5000 nota:latest \
    -e "APPLICATION_ROOT=/api" \
    -e "APPLICATION_POSTGRES_HOST=127.0.0.1" \
    -e "APPLICATION_POSTGRES_USER=docker" \
    -e "APPLICATION_POSTGRES_PW=docker" \
    -e "APPLICATION_POSTGRES_PORT=32772" \
    -e "APPLICATION_POSTGRES_DB=docker" \
    -e "ENVIRONMENT=dev"