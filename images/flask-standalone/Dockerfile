FROM python:3.7-alpine
LABEL maintainer="generic13 at gmail dot com"
LABEL version="1.0"
ENV FLASK_ENV development
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV REFRESHED_AT 2019_08_06
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip; pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
EXPOSE 5000
