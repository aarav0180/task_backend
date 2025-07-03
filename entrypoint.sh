#!/bin/bash
set -e
export DISPLAY=:0
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
