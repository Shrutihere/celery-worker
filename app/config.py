import os


class Settings:
    PORT = os.getenv("PORT", 5000)
    DEBUG_MODE = bool(os.getenv("DEBUG_MODE", False))
    VERSION = "0.23.1"

    MONGODB_URL = os.getenv(
        "MONGODB_URL",
        "mongodb+srv://admin:Kyjkyj-kuzpis-8hiddo@testing-cluster0.93xsd.mongodb.net/admin",
    )

    PWD = os.getcwd()
    GOOGLE_APP_CREDENTIALS = os.getenv(
        "GOOGLE_APP_CREDENTIALS", PWD + "/app/adapters/notifications/keys/google-services.json"
    )

settings = Settings()
