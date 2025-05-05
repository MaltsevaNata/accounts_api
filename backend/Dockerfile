FROM python:3.10-alpine
WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY .. .

RUN chmod +x ./entrypoint.sh
RUN chmod +rwx ./accounts_api/
COPY ./entrypoint.sh /usr/app/entrypoint.sh
RUN chmod +x /usr/app/entrypoint.sh

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/usr/app/entrypoint.sh"]

CMD gunicorn accounts_api.wsgi:application --bind 0.0.0.0:8000 -p 8000 --reload