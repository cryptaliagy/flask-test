FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -e .

CMD /app/entrypoint.sh
