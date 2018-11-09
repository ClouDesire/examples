# python-docker-metric

This project is a simple Docker application that exposes custom metrics.
The project uses as its only dependency [web.py](https://github.com/webpy/webpy)


## Development


### Install virtualenv (optional but very recommended)

`pip install virtualenv && virtualenv --python=/usr/bin/python3 venv`


### Install dependencies

`pip3 install -r requirements.txt`


### Run script

`python3 main.py`


## Docker


### Build Docker container

`docker build -t python-docker-metric .`


### Run Docker container

`docker run -p8080:8080 python-docker-metric`
