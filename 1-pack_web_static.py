#!/usr/bin/python3
"""
Fabric script that generates a tgz archive
from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


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
