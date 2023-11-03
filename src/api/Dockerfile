FROM ubuntu:20.04

WORKDIR /code

ADD ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install python3-pip -y && pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code/src

CMD [ "python3",  "./main.py" ]
