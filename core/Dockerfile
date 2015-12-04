FROM python:3.5

MAINTAINER Artur Zylinski (@ArturZylinski)

RUN pip install --upgrade pip

# add requirements.txt and install
ADD requirements.txt /code/core/requirements.txt
RUN pip install -r /code/core/requirements.txt

RUN PYTHONPATH="$PYTHONPATH:/code/core"

ADD . /code/core
WORKDIR /code/core
