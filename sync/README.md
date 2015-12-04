# Sync module

The most important module within the project.
It's responsiable for connecting to NextBus via API, parse data, and format it in a way, so it would be ready for use, for all other modules (mainly core and stop_finder).

It save the data in both PostgreSQL and ES (*known issue*: with this approach, there's not transactions).


### Possible imporovements

A definitely MUST-HAVE is a celery worker, that would use periodic tasks to synchronize.
There should be one main task, that is triggered every single night, that would fetch the data and prepare time tables for next days. Every agency and route as a separate celery task, so it could be handle retries nicely.

Currently, there's a endpoint ```/run``` that would trigger the entire synchronization at once, which is not ideal.
