from kombu import Queue, Exchange
import os

# BROKER_URL = 'amqp://localhost'

BROKER_TRANSPORT = 'sqs' 

BROKER_USER = os.environ.get('USER')

BROKER_PASSWORD = os.environ.get('PASSWORD')

# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout' : 3600, 'polling_interval': 0.3}


CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('add_queue', Exchange('exchange1'), routing_key='add_key'),
    # Queue('mul_queue', Exchange('exchange1'), routing_key='mul_key'),
    # Queue('build_insight_queue', Exchange('exchange1'), routing_key='build_insight_key'),
    # Queue('ibuilder_queue', Exchange('exchange1'), routing_key='ibuilder_key'),
)

CELERY_ROUTES = {
    'tasks.add': {'queue': 'add_queue'},
    # 'tasks.mul': {'queue': 'mul_queue'},
    # 'tasks.build_insight': {'queue': 'build_insight_queue'},
    # 'ibuilder.sub_build': {'queue': 'ibuilder_queue'},
}

# CELERY_IMPORTS=("tasks","ibuilder",)
CELERY_IMPORTS=("tasks")


# CELERY_RESULT_BACKEND = 'db+postgresql://postgres:postgres@localhost:5432/mycelery_backend'
# CELERY_RESULT_ENGINE_OPTIONS = {'echo': True}