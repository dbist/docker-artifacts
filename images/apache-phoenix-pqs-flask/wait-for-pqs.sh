#!/bin/sh
# wait-for-pqs.sh

set -e

host="$1"
shift
cmd="$@"

echo "!quit" > sqlfile.sql
until $PHOENIX_HOME/bin/sqlline-thin.py http://"$host":8765 sqlfile.sql &> /dev/null; do
  >&2 echo "PQS is unavailable - sleeping"
  sleep 1
done
rm sqlfile.sql

>&2 echo "PQS is up - executing command"
exec $cmd
rm sqlfile.sql
