FROM python:latest
WORKDIR /app

RUN  apt-get update && apt-get install \
     nano \
      -y wget \
      -y git \
      -y python3 \
      -y python3-pip \
      -y python3-dev \
      -y python3-venv \
      -y python3-wheel \
      -y ython3-django 
      

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade wheel
RUN pip install websocket-client
RUN pip install django
RUN pip install requests
RUN pip install json
RUN pip install datetime
RUN pip install channels
RUN python3 -m pip install -U channels

RUN groupadd -g 1000 www 

RUN useradd -u 1000 -g www www


USER  www

COPY  --chown=www:www  . /app

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
