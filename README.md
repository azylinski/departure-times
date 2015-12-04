# Departure Times

Departure Times, Coding Challenge

Demo: http://188.166.69.145/


### General overview

According to problem statement: **as if it were going into production**, I put all my afford to make an back-end architecture scalebale and easy to change.

*Service Oriented Architecture*, with 7 docker containers:
* nginx
* console
* core
* stop_finder
* sync (TODO + RabbitMQ)
* postgres
* elasticsearch

Every modules is described within it's own readme file.


### Preparation

To run an aplication, we just need to clone current repo, run ```docker-compose up -d``` and create ```next_bus``` database in postgresql. Once all services are ready, we can trigger synchronization (```/run``` endpoint in sync module), to fetch data from NextBus.


### Basic workflow

User is coming to the page, he/she should be asked for ```GeoLocation```. Once it's provided, ```stop_fined``` would look in ```elasticsearch``` for nearest stop for given coordinates. When that stop is defined, ```core``` would be asked to give the schedule for given **stopTag**.


### Tools used

* Python 3.5
* docker 1.9, docker-compose 1.5, docker-machine 0.5
* postgresql 9.4, elasticsearch 2.1, (TODO: celery + rabbitmq)
