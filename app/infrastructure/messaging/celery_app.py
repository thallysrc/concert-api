import os
import time
from kombu import Queue

from celery import Celery

celery_app = Celery(
    "campaign_consumer",
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1"),
)


celery_app.conf.task_queues = (
    Queue("email"),
    Queue("whatsapp"),
    Queue("slack"),
)

celery_app.conf.task_routes = {
    "app.tasks.email.*": {"queue": "email"},
    "app.tasks.whatsapp.*": {"queue": "whatsapp"},
    "app.tasks.slack.*": {"queue": "slack"},
}