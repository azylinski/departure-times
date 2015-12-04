# from celery import Celery

from worker.app import create_app
from worker.manager.synchronization_manager import SynchronizationManager


app = create_app()


#
# TODO: Celery web with periodic tasks
#

@app.route("/run")
def hello():
    SynchronizationManager().run()
    return 'OK'


app.run(host="0.0.0.0")

# # Celery configuration
# # app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
#
# # Initialize Celery
# celery = Celery()
#
# @celery.task()
# def add_together(a, b):
#     return a + b
