#!/usr/bin/python3
"""
Fabric script that creates and distributes
an archive to the web servers
"""

from fabric.api import put, run, env, local
from os.path import exists, isdir
from datetime import datetime
env.hosts = ['52.3.245.122', '100.26.223.72']


def do_pack():
    """generates an archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    name = "versions/web_static_{}.tgz".format(date)

    if local("tar -cvzf {} web_static".format(name)).failed is True:
        return None

    return name


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


def deploy():
    """creates and distributes the archive to the servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
