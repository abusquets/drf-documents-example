#!/bin/bash

SCRIPTDIR=`dirname "$BASH_SOURCE"`
MANAGE="$SCRIPTDIR/manage.py"

export ENVIRONMENT_NAME=devel
python -Wall $MANAGE runserver 0.0.0.0:8000
