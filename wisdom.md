Run gunicorn:
```
gunicorn roboao_public.wsgi:application --bind localhost:8001
```

Run supervisord:
```
/data/roboao/anaconda2/bin/python /data/roboao/anaconda2/bin/supervisord -c /data/roboao/dev/roboao-public/supervisord.public.conf
```

Run the following to collect static admin files:
```
python manage.py collectstatic
```