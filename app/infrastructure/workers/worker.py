import os
import time

from celery import Celery

celery_app = Celery(
    "campaign_consumer",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1"),
)


@celery_app.task(bind=True, name="process_campaign")
def process_campaign(self, data: str):

    time.sleep(2)

    result = {"campaign_id": data, "status": "processed"}