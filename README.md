# test-task-for-apptimizm

### Admin - login: admin@admin.ru, password: admin
### Test user - login: test@test.ru, password: test

Python

Разрабатываем систему обеспечивающую работу организации по сдаче автомобилей в аренду.
Пользователь может брать в аренду различные автомобили, и автомобиль может сдаваться
различным пользователям.
У пользователя есть атрибуты email, имя, язык(en, ru). У машин есть атрибуты имя(задается на
двух языках en, ru, реализацию сделать с учетом возможного увеличения языков), год создания, и
дата добавления машины в систему.

Нужно реализовать RestAPI со следующим функционалом:
- зарегистрировать пользователя
- получить машины пользователя
- изменить данные пользователя
- получить всех пользователей
Для api нужно использовать token based authentication.
По RestApi название машины отдается на языке пользователя.

Сайт должен предоставлять следующий функционал:
- зарегистрировать пользователя/войти
- добавить машину в систему
- добавить машину пользователю
- информация о пользователе
- изменить информацию о пользователе
Неавторизованному пользователю доступна только страница зарегистрировать
пользователя/войти, при открытии других страниц неавторизованным пользователем должен
производиться редирект на страницу зарегистрировать пользователя/войти.
При добавлении машины пользователю посылается письмо.
Для авторизации используется пара email-пароль.
Для функционирования системы база данных наполняется тестовыми данными любым удобным
способом.
Для проверки функционирования должен быть написан тестовый сценарий.
Желательно развертывание системы производить через docker-compose.
