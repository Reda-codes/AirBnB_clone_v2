# Web server that servers static content

$configuration = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
                try_files $uri $uri/ =404;
                add_header X-Served-By $hostname;
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
}"

$body = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

package {'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
}

file {'/var/www/html':
  ensure => 'directory',
  mode   => '0777'
}

file {'/etc/nginx/sites-available':
  ensure => 'directory',
  mode   => '0777'
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!'
}

file {'/var/www/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page"
}

file {'/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => $configuration,
}

file {'/data/web_static/releases/test':
  ensure  => 'directory',
}

file {'/data/web_static/shared/':
  ensure  => 'directory',
}

file {'/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => $body,
}

exec {'symbolik link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current'
}

exec {'ownership':
  provider => shell,
  command  => 'sudo chown -hR ubuntu:ubuntu /data/'
}

exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart'
}
