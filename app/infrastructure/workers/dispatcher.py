from celery import chord
from app.infrastructure.messaging.celery_app import celery_app

@celery_app.task(name="aggregate_results")
def aggregate_results(results: list[dict]):
    return {
        "status": "completed",
        "results": results,
    }

@celery_app.task(bind=True, name="process_campaign")
def process_campaign(self, campaign_id: str):
    job = chord(
        [
            celery_app.signature("email.send", args=[campaign_id]),
            celery_app.signature("whatsapp.send", args=[campaign_id]),
            celery_app.signature("slack.send", args=[campaign_id]),
        ],
        celery_app.signature("aggregate_results"),
    )

    result = job.apply_async()
    return result.id