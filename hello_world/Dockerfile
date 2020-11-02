FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirments.txt /code/
RUN pip install -r requirments.txt
COPY . /code/
CMD [ "python", "./manage.py makemigrations","./manage.py makemigrations","./manage.py runserver 0.0.0.0:8000" ]