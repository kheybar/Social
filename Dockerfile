FROM python:latest

WORKDIR /code

COPY requirments.txt /code/

RUN pip install -U pip
RUN pip install -r requirments.txt

COPY . /code/

CMD ["gunicorn", "config.wsgi", ":8000"]