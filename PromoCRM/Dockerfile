FROM python:3.10.4-alpine

RUN mkdir app
WORKDIR /app

COPY . /app

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev postgresql postgresql-contrib
RUN mkdir -p /vol/web/static
RUN chmod a+rw db.sqlite3


RUN pip install -r requirements.txt

EXPOSE 8000

RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
#to start
#docker build -t demo_django .
#docker run -it -p 8000:8000 -d demo_django
#other commands
#docker ps -a
#docker stop demo_django


