# base image  
FROM python:3.11.0 

# where your code lives  
RUN mkdir /ride_on
WORKDIR /ride_on

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

RUN pip install -U pip wheel cmake
# copy whole project to your docker home directory. 

COPY . /ride_on/
# run this command to install all dependencies 
COPY requirement.txt /ride_on/requirement.txt

RUN pip install -r requirement.txt cmake
# port where the Django app runs  
EXPOSE 8000  

# start server  
CMD python manage.py runserver