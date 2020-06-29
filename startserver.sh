#!/bin/bash
dir=$(dirname `dirname "$0"`)
tmux new-session -d -n "SHBM" python3 $dir/manage.py runserver 0.0.0.0:8000 & python3 $dir/manage.py heartmonitor &
