server {
    listen 443 ssl;
    server_name jusan.kz;

    # Пути к SSL сертификатам
    ssl_certificate /etc/nginx/ssl/track-devops.crt;
    ssl_certificate_key /etc/nginx/ssl/track-devops.key;

    # Параметр для dhparam
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;

    # Дополнительные настройки SSL
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers on;

    # Location для /secret_word
    location /secret_word {
        # Возвращаем строку "jusan-nginx-cert" с кодом состояния 201
        return 201 'jusan-nginx-cert';
    }
}
