#!/usr/bin/env python
import os
import sys

sys.path.append('/home/mattias/webapps/yousense_ping')
sys.path.append('/home/mattias/webapps/yousense_ping/latencyping')
sys.path.append('/home/mattias/webapps/yousense_ping/lib/python2.7')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "latencyping.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
