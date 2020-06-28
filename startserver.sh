#!/bin/bash
dir=$(dirname `dirname "$0"`)
echo $dir
tmux new-session -d -n "SHBM" python3 $dir/manage.py runserver & python3 $dir/manage.py heartmonitor &
