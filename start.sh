#!/bin/sh

tmux new-session -d -n "SHBM" gunicorn --bind 127.0.0.1:8000 --access-logfile - --workers 3 --bind unix:/home/wcs/Documents/programming/python/SHBM/SHBM.sock SHBM.wsgi & python3 /home/wcs/Documents/programming/python/SHBM/manage.py heartmonitor &
