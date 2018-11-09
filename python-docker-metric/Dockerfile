FROM python:3.6
LABEL Author="Cloudesire Team <dev@cloudesire.com>"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "main.py" ]
