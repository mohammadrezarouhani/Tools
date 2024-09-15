import logging
import logstash
from redis import Redis
from celery.signals import (
    after_setup_logger,
    after_setup_task_logger,
    worker_init,
    worker_shutdown,
)
from celery.utils.log import get_task_logger

from .task import *

@worker_init.connect
def setup_worker_init(**kwargs):
    # connect_to_mongo()


@worker_shutdown.connect
def setup_worker_shutdown(**kwargs):
    print("bye")
    # close_mongo_connection()


def initialize_logstash(logger=None, loglevel=logging.INFO, **kwargs):
    if not logger:
        logger = get_task_logger(__name__)

    handler = logstash.TCPLogstashHandler(
        "domain", 50000, tags=["test"], version=1
    )
    handler.setLevel(loglevel)
    logger.addHandler(handler)
    return logger


after_setup_task_logger.connect(initialize_logstash)
after_setup_logger.connect(initialize_logstash)
