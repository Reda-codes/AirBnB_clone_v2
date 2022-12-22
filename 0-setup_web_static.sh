#! /usr/bin/env bash
# Script that sets up your web servers for the deployment

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<h1>Hello World<h1>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/curren
t/;\n\t}\n" > /etc/nginx/sites-available/default
sudo service nginx restart
