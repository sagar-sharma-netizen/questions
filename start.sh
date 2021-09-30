#!/bin/bash

# NAME OF THE APPLICATION
NAME="questions"

# DJANGO PROJECT DIRECTORY
DJANGO_DIR=$PWD

# SOCKET FILE
SOCKET_FILE=run/gunicorn.sock

# USER
USER=ubuntu

# GROUP
GROUP=ubuntu

# NUMBER OF WORKERS
NUM_WORKERS=3

# SETTING MODULE
DJANGO_SETTINGS_MODULE=questions.settings

# WSGI MODULE NAME
DJANGO_WSGI_MODULE=questions.wsgi

echo "Starting $NAME as `whoami`"

# ACTIVATING THE VIRTUAL ENVIRONMENT
cd $DJANGO_DIR

#source venv/bin/activate

# CREATE VIRTUAL ENV
virtualenv -p python3 venv

# ACTIVATE VIRTUAL ENV
source venv/bin/activate

# INSTALL REQUIREMENTS
pip install -r requirements.txt

# EXPORT SETTINGS
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

export PYTHONPATH=$DJANGO_DIR:$PYTHONPATH

# CREATE RUN DIRECTORY IF IT DOES NOT EXIST
RUNDIR=$(dirname $SOCKET_FILE)

test -d $RUNDIR || mkdir -p $RUNDIR

# COLLECT STATIC FILES
python manage.py collectstatic -c --no-input

# START GUNICORN

# PROGRAMS MEANT TO BE RUN UNDER SUPERVISION SHOULD NOT BE DAEMONIZED (DON'T USE --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
#--user=$USER --group=$GROUP \
--bind=unix:$SOCKET_FILE \
--log-level=debug \
--log-file=-