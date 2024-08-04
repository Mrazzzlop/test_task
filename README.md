# Тестовое задание на позицию Backend-разработчик на языке Python.



[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)

## Запуск проекта.

### Клонируйте репозиторий с проектом на свой компьютер. В терминале из рабочей директории выполните команду:
```bash
git clone https://github.com/Mrazzzlop/foodgram-project-react.git
```

### Установить и активировать виртуальное окружение

```bash
source /venv/bin/activate
```

### Установить зависимости из файла requirements.txt

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
### Создать файл .env в папке проекта:
```.env
SECRET_KEY=secret_key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,backend
```

### Выполните миграции:
```bash
python manage.py migrate
```
### Заполните базу данными: 
```bash
python manage.py load_ads
```
### Запустите сервер 
```bash
python manage.py runserver
```

## Примеры

### Запросы к API

Регистрация:

```
http://127.0.0.1:8000/api/register/
```

```
{
  "email": "user@example.com",
  "username": "string"
  "password": "string"
}
```
Аутентификация
```
http://127.0.0.1:8000/api/login
```

```
{
  "email": "string",
  "password": "string"
}
```

Получить список объявления по id:
Только для авторизованных пользователей.(Bearer token)

```
http://127.0.0.1:8000/api/advertisements/<int:ad_id>/
```

```
{
    "title": "Установка, монтаж и настройка систем видеонаблюдения",
    "id": 2,
    "author": "Сервис Про",
    "views": 1014,
    "position": 2
}
```
