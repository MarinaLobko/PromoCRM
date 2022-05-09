FROM python:3.10.4

WORKDIR /app

COPY requirments.txt /app/requirments.txt

RUN pip install -r requirments.txt

COPY . .

EXPOSE 8000

RUN ["python", "manage.py", "migrate"]

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver" , "0:8000"]

#to start
#docker build -t demo_django .
#docker run -it -p 8000:8000 -d demo_django
#other commands
#docker ps -a
#docker stop demo_django