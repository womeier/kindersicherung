#!/usr/bin/env bash


if [[ $EUID -ne 0 ]]; then
	echo "this script needs to be run as root."
	exit 1
fi


cat > /etc/cron.d/kindersicherung << EOF
# Kindersicherung: hosts blocking

@reboot root /etc/hosts.d/run.py
EOF
