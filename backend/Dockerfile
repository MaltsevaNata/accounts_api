FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    netcat-openbsd

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

COPY ./entrypoint.sh /usr/app/entrypoint.sh
RUN chmod +x /usr/app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/usr/app/entrypoint.sh"]

CMD ["gunicorn", "accounts_api.wsgi:application", "--bind", "0.0.0.0:8000"]