server {
    listen 8080;
    server_name example.com;

    # Логирование
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    # Основной блок, обрабатывающий корень (index.html)
    location / {
        root /var/www/site;
        index index.html;
    }

    # Блок для пути /images
    location /images {
        auth_basic "Restricted Area";
        auth_basic_user_file /etc/nginx/.htpasswd_design;
        root /var/www/site;
        try_files $uri $uri/ =404;
    }

    # Блок для пути /gifs
    location /gifs {
        auth_basic "Restricted Area";
        auth_basic_user_file /etc/nginx/.htpasswd_marketing;
        root /var/www/site;
        try_files $uri $uri/ =404;
    }

    # Остальные конфигурации
    # ...
}
