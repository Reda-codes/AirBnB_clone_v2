#! /usr/bin/env bash
# Script that sets up your web servers for the deployment
sudo mkdir -p /data/web_static/releases/test
sudo echo "<h1>Hello World<h1>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
                try_files $uri $uri/ =404;
                add_header X-Served-By "$hostname";
    }
    location /redirect_me{
        return 301 https://www.youtube.com/watch?v=y6120QOlsfU;
    }

    location /hbnb_static{
        alias /data/web_static/current/;
    }

    error_page 404 /custom_404.html;
    location /custom_404.html {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx start
