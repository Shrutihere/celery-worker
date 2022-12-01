from firebase_admin import messaging

from src.interfaces.notification.models.Common import NotificationInputModel


class CommonNotification:
    """
    This class does xyz
    """

    model = None

    def __init__(self, model: NotificationInputModel):
        """
        :param: this param is for xyz
        """
        self.model = model.dict()

    def create(self):
        return messaging.Notification(
            title=self.model["title"],
            body=self.model["body"],
            image=self.model["image"],
        )
