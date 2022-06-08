FROM python:3.10

WORKDIR /work

COPY requirements.txt .

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt && rm requirements.txt

COPY exerciseapp .

CMD export FLASK_APP=app && flask run