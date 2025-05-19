#!/bin/bash
set -e

echo "Checking if the 'user' table exists in MySQL..."

TABLE_EXISTS=$(mysql -h db -uadmin -padmin123 -Dusermanagement -e "SHOW TABLES LIKE 'user';" | grep user || true)

if [ -z "$TABLE_EXISTS" ]; then
  echo "'user' table does not exist. Running Alembic migrations..."
  alembic upgrade head
else
  echo "'user' table exists. Skipping Alembic migrations."
fi

echo "Running insert.py to seed initial data..."
python insert_data.py

echo "Starting FastAPI app..."
exec uvicorn UserManagement.main:app --host 0.0.0.0 --port 8085 --reload
