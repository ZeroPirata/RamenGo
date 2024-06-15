FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/logs
COPY .env .env
RUN apt-get update && apt-get install -y netcat-openbsd

ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=ramengo_db
ENV POSTGRES_SCHEMA=public
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV PATH_LOGGER=/app/logs/log.log

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
