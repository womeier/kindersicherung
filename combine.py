#!/usr/bin/env python3

from datetime import datetime
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def base():
    with open(os.path.join(BASE_DIR, "base")) as f:
        return f.read()


def block(path):
    hosts = ""
    with open(path) as f:
        for address in f.read().strip().split("\n"):
            hosts += f"0.0.0.0   {address}\n"
            hosts += f"0.0.0.0   www.{address}\n"

    return hosts


HOSTS = base()
HOSTS += block(os.path.join(BASE_DIR, "blocked-perm"))

# block sites except on Friday
#
# Monday = 0, Friday = 4
if datetime.today().weekday() != 4:
    HOSTS += "\n"
    HOSTS += block(os.path.join(BASE_DIR, "blocked-tmp"))

if os.geteuid() != 0:
    print("Script should be run as root.")
    exit(1)

with open("/etc/hosts", "w") as f:
    f.write(HOSTS)
