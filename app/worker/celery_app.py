from celery import Celery

celery = Celery('worker', backend='rpc://', broker='amqp://guest:guest@127.0.0.1:5672//')    # running locally
# celery = Celery('worker', backend='rpc://', broker='pyamqp://guest@rabbitmq//')    # running through docker


celery.conf.task_routes = {
        "app.worker.celery_worker.test_celery": "test-queue"}

celery.conf.update(imports=['app.worker.celery_worker'])

# celery.conf.beat_schedule = {
#         "run-me-every-ten-seconds": {
#         "task": "app.worker.celery_worker.test_celery",
#         "schedule": 10.0,
#         "args": ["word"]
#         }
# }

# ----------command to start worker----------
# celery -A tasks worker -l info -P eventlet
# celery -A app.worker.celery_app worker --loglevel=info -Q test-queue -P eventlet
# celery -A app.worker.celery_app flower --port=5555
# celery -A app.worker.celery_app beat --loglevel=INFO -s celery_file