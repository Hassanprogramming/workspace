from django.db import models
import json

class Log(models.Model):
    
    TYPE_CHOICES = [
        ('Person', 'Person'),
        ('Face', 'Face'),
        ('Bag', 'Bag'),
    ]
    
    stream_id = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=1, choices=[('D', 'Danger'), ('S', 'Safe')])  # 'D' for danger and 'S' for safe
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    coordinates = models.JSONField()
    thumbnail = models.TextField()
    session_id = models.UUIDField()

    def __str__(self):
        return f"Log - Stream ID: {self.stream_id}"

    @classmethod
    def create_from_json(cls, json_data):
        log_data = json_data.get("log", {})
        return cls(
            stream_id=json_data["stream_id"],
            timestamp=json_data["timestamp"],
            status=json_data["status"],
            type=log_data.get("type", ""),
            coordinates=log_data.get("coordinates", []),
            thumbnail=log_data.get("thumbnail", ""),
            session_id=json_data["session_id"],
        )
