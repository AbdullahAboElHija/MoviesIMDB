##!/bin/bash
#DIRECTORY=./shared
#DONE_FILE_NAME=migration.done
#
#if [ !  -d "$DIRECTORY" ]; then
#  echo "create $DIRECTORY "
#  mkdir $DIRECTORY
#fi
#echo "crcheck if $DIRECTORY/$DONE_FILE_NAME  exists "
#if  [ ! -f  $DIRECTORY/$DONE_FILE_NAME ]; then
#    echo "Start mysql db migration"
#    mysql -h db -p$SQL_ROOT_PASSWORD  < data.sql
#    touch $DIRECTORY/$DONE_FILE_NAME
#fi


#!/bin/bash
DIRECTORY=./shared
DONE_FILE_NAME=migration.done

# Check for directory
if [ ! -d "$DIRECTORY" ]; then
  echo "create $DIRECTORY"
  mkdir $DIRECTORY
fi

# Check if the database is ready
echo "Waiting for MySQL to initialize the database..."
until mysql -h $SQL_HOST -u$SQL_USER -p$SQL_PASSWORD -e "USE $SQL_DATABASE"; do
  echo "Database not yet available. Waiting..."
  sleep 5
done
echo "Database is available!"

echo "Check if $DIRECTORY/$DONE_FILE_NAME exists"
if [ ! -f "$DIRECTORY/$DONE_FILE_NAME" ]; then
    echo "Start MySQL db migration"
    mysql -h db -p$SQL_ROOT_PASSWORD -D $SQL_DATABASE < data.sql
    touch "$DIRECTORY/$DONE_FILE_NAME"
fi
