FROM python:3.10

WORKDIR /work

COPY requirements.txt .

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt && rm requirements.txt

COPY exerciseapp .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]