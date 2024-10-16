FROM python:3.9

WORKDIR /django

ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py","runserver","0.0.0.0:8000" ]