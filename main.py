from app.worker.celery_app import  celery


# app = FastAPI(title="Celery API", version=settings.VERSION)

# #
# @app.on_event("startup")
# async def startup_db_client():
#     # app.mongodb = AsyncIOMotorClient(settings.MONGODB_URL)
#     # app.firebase = firebase_admin.initialize_app(
#     #     credentials.Certificate(settings.GOOGLE_APP_CREDENTIALS)
#     # )
#     pass


# app.include_router(tasks_router)

if __name__ == "__main__":
    celery.start(["worker", "--loglevel=INFO", "-P", "eventlet", "-Q", "test-queue"])
