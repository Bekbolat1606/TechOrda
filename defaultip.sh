server {
    listen 8080;
    server_name example.com;

    # Location для /secret_word
    location /secret_word {
        # Возвращаем строку "jusan-nginx-ip" с кодом состояния 203
        return 203 'jusan-nginx-ip';
        
        # Разрешаем доступ из подсети 192.0.0.1/20, но исключаем 192.0.0.1
        allow 192.0.0.1/20;
        deny 192.0.0.1;

        # Запрещаем доступ для всех остальных
        deny all;
    }
}
