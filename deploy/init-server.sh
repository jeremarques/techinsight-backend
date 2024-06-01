#!/bin/sh

gunicorn techinsight.wsgi --bind 0.0.0.0:80