FROM python:3.10.8-alpine3.16

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "retweet.py"]

