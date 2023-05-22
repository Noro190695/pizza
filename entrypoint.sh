python3 manage.py migrate
#python3 manage.py initadmin
python3 manage.py collectstatic --noinput
gunicorn pizza.wsgi:application --bind :$PORT --workers 1 --threads 8 --timeout 0
