#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

echo "Deployment begins.."

# Updating the packages
sudo apt-get -y update
sudo apt-get -y install nginx
echo "Packages updated"

# Configuring firewalls
sudo ufw allow 'Nginx HTTP'
echo "Allow NGINX HTTP connections"

# Creating directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "folders created"

# Testing string added
echo "<h1>Welcome to www.viestar.tech</h1>" > /data/web_static/releases/test/index.html
echo "index added"

# Overwrite prevented
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;

# Symbollic links created
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo "Symbolic link created"

# Restart server
sudo service nginx restart
echo "restarted NGINX"
