FROM python:3.8

WORKDIR /Ejemplo_csv
COPY requirements.txt /Ejemplo_csv/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Ejemplo_csv/requirements.txt

COPY . /Ejemplo_csv

#que contenedor este encendido
CMD bash -c "while true; do sleep 1; done"