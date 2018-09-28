#!/bin/bash

SCRIPTDIR=`dirname "$BASH_SOURCE"`
MANAGE="$SCRIPTDIR/manage.py"

export ENVIRONMENT_NAME=test
python -Wall $MANAGE test "$@"
