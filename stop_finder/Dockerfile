FROM python:3.5

MAINTAINER Artur Zylinski (@ArturZylinski)

RUN pip install --upgrade pip

# add requirements.txt and install
ADD requirements.txt /code/stop_finder/requirements.txt
RUN pip install -r /code/stop_finder/requirements.txt

RUN PYTHONPATH="$PYTHONPATH:/code/stop_finder"

ADD . /code/stop_finder
WORKDIR /code/stop_finder
