web: gunicorn django_news_aggregator.wsgi:application --log-file -
celery: celery -A django_news_aggregator worker -l info
celerybeat: celery -A django_news_aggregator beat -l info