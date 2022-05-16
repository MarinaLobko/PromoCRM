FROM python:3.10.4

RUN mkdir app
WORKDIR /app

COPY . /app

RUN chmod a+rw db.sqlite3

RUN pip install -r requirements.txt

EXPOSE 8000

RUN ["python", "manage.py", "migrate"]

#CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
#to start
#docker build -t demo_django .
#docker run -it -p 8000:8000 -d demo_django
#other commands
#docker ps -a
#docker stop demo_django


