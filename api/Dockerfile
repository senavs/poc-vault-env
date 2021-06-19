FROM python:3.9-alpine3.12

COPY . /code/api

WORKDIR /code

RUN pip install -r api/requirements.txt

CMD ["python", "-m", "api"]
