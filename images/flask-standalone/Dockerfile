FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP flaskr flask init-db
ENV FLASK_APP flaskr
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip; pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
EXPOSE 5000
