FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /parking
WORKDIR /parking
ADD . /parking/ 
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT
