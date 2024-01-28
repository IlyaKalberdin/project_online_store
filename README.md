# Проект по блоку Django, онлайн магазин.   

Для отправки письма при достижения 100 просмотров с вашей почты, 
создайте переменные окружения:
1) EMAIL_HOST_USER - адрес почты name@yandex.ru;
2) EMAIL_HOST_PASSWORD с паролем приложения.

Инструкция https://yandex.ru/support/mail/mail-clients/others.html. Раздел "Настроить только отправку по протоколу SMTP"

В переменной EMAIL_TO в файле blog_app/views.py укажите email на который хотите 
отправлять письмо.