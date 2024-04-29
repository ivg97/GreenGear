# GreenGear

## Перед началом работы

```

$ mkdir GreenGear
$ cd GreenGear/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd green_gear
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ pythom3 manage.py runserver

```
Переходим на http://localhost:8000/.
Получаем начальную страницу django или конкретный шаблон:
![img.png](img.png)

## Обновление миграций

```
$ pwd
/home/user/GreenGear/green_gear

$  python3 manage.py migrate
Operations to perform:
  Apply all migrations: about_us, admin, auth, blog, contact, contenttypes, service, sessions
Running migrations:
  Applying about_us.0001_initial... OK
  Applying blog.0001_initial... OK
  Applying contact.0001_initial... OK
  Applying service.0001_initial... OK
  Applying sessions.0001_initial... OK

```

## Создание суперпользователя

```
$ pwd
/home/user/GreenGear/green_gear

$ python3 manage.py createsuperuser
Username (leave blank to use 'user'): 
Email address: 
Password: 
Password (again): 
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

```

## Правила работы
1. Новый функционал -> новая ветка. Потом мерж в основную
2. В основной ветке ничего не правим. Только через мерж.
3. main - продакшен
