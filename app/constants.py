TIMELINE_MODULE = "timeline"

DEBUG = "http://localhost:4000"
PROD = "https://main.fastapi.edvora.me"

TIMELINE_NOTIFICATION_ENDPOINT_DEBUG = DEBUG + "/notifications/classroom"
TIMELINE_NOTIFICATION_ENDPOINT_PROD = PROD + "/notifications/classroom"

USERS_NOTIFICATION_ENDPOINT_DEBUG = DEBUG + "/notifications/users"
USERS_NOTIFICATION_ENDPOINT_PROD = PROD + "/notifications/users"

STATE_PRESENT = 1