release:python manage.py makemigrations ---no-input
release:python manage.py migrate ---no-input
web: gunicorn reservation.wsgi:application --log-file -
python manage.py collectstatic --noinput

