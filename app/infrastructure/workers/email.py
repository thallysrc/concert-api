import time

from app.infrastructure.messaging.celery_app import celery_app


@celery_app.task(name="ses.send", queue="ses")
def send_mail(campaign_id: str):

    for _i in range(30):
        print("Sending email...", _i)
        time.sleep(1)

    return {"ses": "sent", "campaign_id": campaign_id, "total": 30}