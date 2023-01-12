#!/usr/bin/python3
"""
Fabric script that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.3.245.122', '100.26.223.72']


def do_deploy(archive_path):
    """Code to execute"""
    if exists(archive_path) is False:
        return False
    try:
        filee = archive_path.split("/")[-1]
        ext = filee.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filee, path, ext))
        run('rm /tmp/{}'.format(filee))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext))
        run('rm -rf {}{}/web_static'.format(path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except Exception:
        return False
