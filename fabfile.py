#!/usr/bin/env python
# As close to Python3 as 2.7 can get
from __future__ import absolute_import, division, print_function, unicode_literals
from future_builtins import *  # ascii, filter, hex, map, oct, zip

from fabric.api import *
from os.path import join as oj
from os.path import dirname as up

env.hosts = ['mattias@mattias.linnap.com']
REMOTE_DIR = '/home/mattias/webapps/yousense_ping/latencyping'

@task
def push_tarball():
    local('tar czf tarball.tar.gz *')
    run('rm -rf ' + REMOTE_DIR)
    run('mkdir ' + REMOTE_DIR)
    put('tarball.tar.gz', oj(REMOTE_DIR, 'tarball.tar.gz'))
    local('rm tarball.tar.gz')
    with cd(REMOTE_DIR):
        run('tar xzf tarball.tar.gz')
        run('rm tarball.tar.gz')


@task
def restart_apache():
    run(oj(up(REMOTE_DIR), 'apache2/bin/restart'))


@task
def deploy():
    push_tarball()
    restart_apache()
