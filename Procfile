web: gunicorn reservation.wsgi
python manage.py collectstatic --noinput
release: python manage.py migrate
