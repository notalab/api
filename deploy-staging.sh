#!/bin/bash
echo "Pulling latest version from staging"
git fetch --all && git checkout staging
git pull
#cp .env.example .env

echo "Installing server dependencies"
docker-compose run --rm server pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

echo "Upgrading database"
docker-compose run --rm server python src/manage.py db upgrade

echo "Restarting daemon"
docker-compose stop
docker-compose up -d server

echo "Finished"
git status
