# t 

Для запуска приложения необходимо:

- git clone...
- `docker run --name rs -p 6379:6379 -d redis:6.0.5-alpine`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- отредактировать пути в `celery_app.conf`
- `celery worker -A app --loglevel=info`
- `python manage.py runserver`

В браузере перейти по адресу http://127.0.0.1:8000/snippets/form/