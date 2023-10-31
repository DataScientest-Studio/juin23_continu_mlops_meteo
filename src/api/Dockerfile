FROM ubuntu:20.04

# ENV secret d05669a75db8538349e3cfbe3c8d0b13f9b4cddc6725602e74ffe7fb981e31d8
# ENV algorithm H256

WORKDIR /code

ADD ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install python3-pip -y && pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

#ADD ../src/ /code/src/

#ADD ../../models/model.pkl /code/models/model.pkl

#ADD ./main.py /code/main.py

WORKDIR /code/src

#EXPOSE 8085

CMD [ "python3",  "./main.py" ]
