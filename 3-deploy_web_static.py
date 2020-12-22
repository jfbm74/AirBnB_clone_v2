#!/usr/bin/python3
""" Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy
"""
from datetime import datetime
from fabric.api import *
from os.path import isfile

env.host = ["35.196.37.49", "35.237.193.55"]


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    today = datetime.now().strftime("%Y%m%d%H%M%S")
    namefile = "versions/web_static_{}.tgz".format(today)
    compress = "tar -cvzf {} web_static".format(namefile)
    if local(compress) == 1:
        return None
    return namefile


def do_deploy(archive_path):
    """
        Distributes an archive to servers
    """
    if isfile(archive_path) is False:
        return False

    try:

        namefile = archive_path.split("/")[1].split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(namefile))
        run(" tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(namefile, namefile))
        run("rm /tmp/{}.tgz".format(namefile))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(namefile, namefile))
        run("rm -rf /data/web_static/releases/{}/web_static".format(namefile))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(namefile))

    except Exception:
        return False
    return True


def deploy():
    """
        compress and deploy a tar file to a web server
    """
    archive_path = do_pack()

    if archive_path is None:
        return False
    return do_deploy(archive_path)
