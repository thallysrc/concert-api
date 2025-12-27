import time

from app.infrastructure.messaging.celery_app import celery_app


@celery_app.task(name="slack.send", queue="slack")
def send_slack(campaign_id: str):
    for _i in range(40):
        print("Sending email...", _i)
        time.sleep(1)
    return {"slack": "sent", "campaign_id": campaign_id, "total": 40}