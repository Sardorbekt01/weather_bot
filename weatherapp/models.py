from django.db import models


class WeatherMessage(models.Model):
    sent_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    recipient_email = models.EmailField()

    def __str__(self):
        return f"Sent at {self.sent_time} to {self.recipient_email}"
