#Vamos a construir nuestra imagen de docker a nuestra necesidad, basandonos en una imagen ya construida de python

FROM python:3.12-bookworm

RUN apt-get update && apt-get install python3-dev libgdal-dev graphviz graphviz-dev -y --force-yes

#Cuando la imagen de docker arranque queda parada en esta carpeta y debe coincidir donde montamos nuestro código fuente 
WORKDIR /usr/src/app 

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8000

# 1. ya tenemos el djangoadmin, le pasamos un comando, el nombre del proyecto, y en que carpeta se instalará (en este caso . es en la que estamos) pero tiene un error conceptual ya que como recien se crea la carpeta en verdad no puede ejecutar esta carpeta doasd
#RUN django-admin startproject app .

#comando que ejecute una vez que levante la imagen cada vez

CMD ["python","manage.py","runserver","0.0.0.0:8000"]




