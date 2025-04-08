
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AnalyticsEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event_type} at {self.timestamp}"

