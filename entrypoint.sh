#!/bin/bash

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Aguardando o PostgreSQL estar disponível em $POSTGRES_HOST:$POSTGRES_PORT..."
  sleep 1
done
echo "PostgreSQL está pronto!"

alembic revision --autogenerate -m "Generate new migration"
alembic upgrade head

export PYTHONPATH=/app
python /app/src/database/inserts.py

exec "$@"
