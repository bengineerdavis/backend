#!/bin/bash
set -e

echo "DO_STAGING_DB_USER: $DO_STAGING_DB_USER"
echo "DO_STAGING_DB_HOST: $DO_STAGING_DB_HOST"
echo "DO_STAGING_DB_PORT: $DO_STAGING_DB_PORT"
echo "DO_STAGING_DB_NAME: $DO_STAGING_DB_NAME"
echo "CB_IMAGE_TAG: $CB_IMAGE_TAG"
echo "GITHUB_ACTOR: $GITHUB_ACTOR"

export STAGING_DB_URL="postgres://$DO_STAGING_DB_USER:$DO_STAGING_DB_PASSWORD@$DO_STAGING_DB_HOST:$DO_STAGING_DB_PORT/$DO_STAGING_DB_NAME"

docker login docker.pkg.github.com -u $GITHUB_ACTOR -p $GITHUB_TOKEN

docker-compose -f docker-compose-prod.yaml down
docker-compose -f docker-compose-prod.yaml up
