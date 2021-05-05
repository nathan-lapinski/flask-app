#!/bin/sh

echo "waiting for postgres..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python3.9 manage.py run -h 0.0.0.0