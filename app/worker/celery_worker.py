from .celery_app import celery
from .tasks import RepeatTask
from app.adapters.notifications.methods.edvora_notification import EdvoraNotification
# from app.adapters.notifications.methods.notification_types import (
#     title_from_type,
#     create_title,
# )
# from app.adapters.notifications.constants import (
#     EVENT_CREATED,
#     TIMELINE_SESSION
# )



@celery.task(base=RepeatTask, acks_late=True, queue="test-queue", name="app.worker.celery_worker.test_celery")
def test_celery(*args, **kwargs) -> str:

    EdvoraNotification(
            auth_header=kwargs["notification_metadata"]["auth_header"],
            title=kwargs["notification_metadata"]["title"],
            body=kwargs["notification_metadata"]["body"],
            item_id=kwargs["notification_metadata"]["item_id"],
            created_at=kwargs["notification_metadata"]["created_at"],
            created_by=kwargs["notification_metadata"]["created_by"],
            classroom_id=kwargs["notification_metadata"]["classroom_id"],
            kind=kwargs["notification_metadata"]["kind"],
        ).send()

    return {
        'args': args,
        'kwargs': kwargs,
    }
