#!/bin/sh

set -x
echo "Check connect db ..."

if [[ ${POSTGRES_HOST} ]]; then
    export PGPASSWORD=${POSTGRES_PASSWORD}
    until psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_NAME -c '\l'; do
      >&2 echo "Postgres is unavailable - sleeping"
      sleep 1
    done
    >&2 echo "Postgres is up - continuing"
    psql -h $POSTGRES_HOST -U $POSTGRES_USER -d template1 -c 'create extension hstore;'
    unset PGPASSWORD
fi

echo "Starting backend ..."

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py loaddata fixtures/*.json
gunicorn -b 0:8000 project.wsgi:application

echo "End"
