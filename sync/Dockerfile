FROM python:3.5

MAINTAINER Artur Zylinski (@ArturZylinski)

RUN pip install --upgrade pip

# add requirements.txt and install
ADD requirements.txt /code/sync/requirements.txt
RUN pip install -r /code/sync/requirements.txt

RUN PYTHONPATH="$PYTHONPATH:/code/sync"

ADD . /code/sync
WORKDIR /code/sync
