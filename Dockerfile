FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD celery -A parser_project worker --loglevel=info & celery -A parser_project beat --loglevel=info && python manage.py runserver 0.0.0.0:8000

