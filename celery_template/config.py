from celery import Celery
from celery.utils.log import get_task_logger
from kombu import Exchange, Queue

from core import settings
from core.celery_config import get_all_workers

app = Celery(
    "tasks",
    broker=settings.REDIS_BROKER,
    backend=settings.REDIS_BACKEND,
    broker_connection_retry_on_startup=True,
)
app.conf.broker_connection_timeout = 300
app.conf.broker_transport_options = {
    "visibility_timeout": 99999999999999,
}
app.conf.result_backend_transport_options = {"visibility_timeout": 99999999999999}
app.conf.visibility_timeout = 99999999999999

workers = get_all_workers()
app.conf.task_queues = [
    Queue(
        name=i[0],
        exchange=Exchange(i[0]),
        routing_key=i[0],
        queue_arguments={"x-max-priority": 10},
    )
    for i in workers
]

app.conf.task_queue_max_priority = 10
app.conf.task_default_priority = 5


logger = get_task_logger(__name__)
