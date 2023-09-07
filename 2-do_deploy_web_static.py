#!/usr/bin/python3
'''
fabric script to distribute an archive to web servers
'''

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['34.138.32.248', '3.226.74.205']


def do_deploy(archive_path):
    """Distributes an archive to a web server anytime.
    Args:
        archive_path (str): The path.
    Returns:
        False.
        Otherwise - True.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    current_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """Deploys the statics to host servers.
    Args:
        archive_path (str): The path to the archived statics.
    """
    if not os.path.exists(archive_path):
        return False
    fi_name = os.path.basename(archive_path)
    fol_name = fi_name.replace(".tgz", "")
    fol_path = "/data/web_static/releases/{}/".format(fol_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(fi_name))
        run("mkdir -p {}".format(fol_path))
        run("tar -xzf /tmp/{} -C {}".format(fi_name, fol_path))
        run("rm -rf /tmp/{}".format(fi_name))
        run("mv {}web_static/* {}".format(fol_path, fol_path))
        run("rm -rf {}web_static".format(fol_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(fol_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
