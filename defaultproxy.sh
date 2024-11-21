server {
    listen 8080;
    server_name localhost;

    # Обслуживание index.html
    location / {
        root /var/www/html;  # Путь к директории, где находится index.html
        index index.html;
    }

    # Обработчик для /api
    location /api/ {
        rewrite ^/api/(.*)$ /$1 break;  # Удаляем /api из URI
        proxy_pass http://localhost:9090;  # Перенаправляем на сервер, работающий на localhost:9090
    }
}
