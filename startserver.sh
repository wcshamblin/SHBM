#!/bin/bash
dir=$(dirname `dirname "$0"`)
tmux new-session -d -n "SHBM" python3 $dir/manage.py runserver & python3 $dir/manage.py heartmonitor &