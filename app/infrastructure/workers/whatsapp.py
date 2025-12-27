import time

from app.infrastructure.messaging.celery_app import celery_app


@celery_app.task(name="whatsapp.send", queue="whatsapp")
def send_whatsapp(campaign_id: str):
    for _i in range(20):
        print("Sending email...", _i)
        time.sleep(1)
    return {"whatsapp": "sent", "campaign_id": campaign_id, "total": 20}