from django.db import models

# Create your models here.

class Log(models.Model):
    stream_id = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=1)
    type = models.CharField(max_length=10)
    coordinates = models.JSONField()
    thumbnail = models.TextField()
    session_id = models.UUIDField()

    def __str__(self):
        return f"Log - Stream ID: {self.stream_id}"
