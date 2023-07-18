# Сервис Insurance Cost
____


## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

____

## Описание проекта

Insurance Cost это ресурс для расчета стоимости страховки груза.  
Пользователи могут запрашивать стоимость страховки для определенного вида груза в определенную дату.

## Установка проекта локально:

### Клонировать репозиторий:
```python
    git clone git@github.com:Rinko69/insurance-cost.git
```
### Cоздать и активировать виртуальное окружение:

```python
python -m venv env
```

```python
source env/bin/activate
```

### Cоздайте файл `.env` в директории `/infra/` с содержанием:

```
- DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
- DB_NAME=postgres # имя базы данных
- POSTGRES_USER=username # логин для подключения к базе данных
- POSTGRES_PASSWORD=password # пароль для подключения к БД (установите свой)
- DB_HOST=db # название сервиса (контейнера)
- DB_PORT=5432 # порт для подключения к БД
```
### Перейти в директирию и установить зависимости из файла requirements.txt:

```python
cd backend/
pip install -r requirements.txt
```

### Выполните миграции:

```python
python manage.py migrate
```

### Запустите сервер:
```python
python manage.py runserver
```

## Запуск проекта в Docker контейнере:

### Установите Docker:

Параметры запуска описаны в файлах `docker-compose.yml` и `nginx.conf` которые находятся в директории `infra/`.  
При необходимости добавьте/измените адреса проекта в файле `nginx.conf`

### Запустите docker compose:
```python
docker-compose up -d --build
```  
  > После сборки появляются 3 контейнера:
  > 1. контейнер базы данных **db**
  > 2. контейнер приложения **backend**
  > 3. контейнер web-сервера **nginx**
### Примените миграции:
```python
docker-compose exec backend python manage.py migrate
```
### Загрузите данные о товарах:
```python
docker-compose exec backend python manage.py load_ingrs
```
### Соберите статику:
```python
docker-compose exec backend python manage.py collectstatic --noinput
```

**Теперь проект готов к работе и доступен по адресу http://domain1.com.**
____

## Руководство к проекту:
### Возможности:
Пользователь может запрашивать стоимость страховки груза на определенную дату.
____

## Ресурсы сервиса API Foodgram:
- rate: коэффициент.
- cargo_type: вид груза.
- cost: цена.
- insurance_cost: стоимость страховки.