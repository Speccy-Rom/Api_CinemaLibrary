# API_CinemaLibrary
API для проекта "Библиотека онлайн фильмов"

##### _разработка Spiridonov R.A aka Speccy_

## Описание ТЗ:
"Библиотека онлайн фильмов" на Django Rest Framework.
  * Категории
  * Жанры
  * Фильмы
  * Кадры из фильма
  * Режиссеры\Актеры
  * Звезды рейтинга
  * Отзывы
  * Фильтры


## Окружение проекта:
  * python 3.9
  * Django 3.1.6
  * djangorestframework
  * Postgresql

Склонируйте репозиторий с помощью git

    https://github.com/Speccy-Rom/Api_CinemaLibrary.git
Перейти в папку:
```bash
cd API_CinemaLibrary
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:

```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/


#### _Документация API_ (автодокументирование API на swagger доступно по адресу ) http://127.0.0.1:8000/swagger/