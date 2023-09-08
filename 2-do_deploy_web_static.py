#!/usr/bin/python3
"""Distributes an archive to your web servers"""
from fabric.api import local, put, run, env
from os.path import exists
from datetime import datetime
import os
import fabric

env.hosts = ['100.25.142.238', '54.197.132.159']
env.user = '<ubuntu>'
env.key_filename = '~/.ssh/id_rsa'
env.use_ssh_config = False


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    archive = "web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    result = local("tar -cvzf versions/{} web_static".format(archive))
    if result.succeeded:
        return "versions/{}".format(archive)
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        archive_filename = os.path.basename(archive_path)
        archive_name = archive_filename.split(".")[0]
        remote_path = "/data/web_static/releases/{}".format(archive_name)
        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, remote_path))

        # Delete the archive from /tmp/
        run("rm /tmp/{}".format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run("rm -f /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(remote_path))

        return True

    except Exception:
        return False


if __name__ == "__main__":
    archive_path = do_pack()
    if archive_path:
        result = do_deploy(archive_path)
        if result:
            print("New version deployed!")
        else:
            print("Deployment failed.")
    else:
        print("Packaging of the archive failed.")
