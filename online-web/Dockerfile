FROM python:3.9-slim

WORKDIR /app

COPY app/ /app/

RUN pip install -r requirements.txt

EXPOSE 9090

CMD [ "python","app.py" ]
