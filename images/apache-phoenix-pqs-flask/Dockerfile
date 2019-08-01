FROM python:3.7-alpine
LABEL maintainer="generic13 at gmail dot com"
LABEL version="1.0"
ENV REFRESHED_AT 2019_08_01
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip; pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
