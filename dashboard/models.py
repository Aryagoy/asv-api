from django.db import models
from uuid import uuid4

# Create your models here.
class Horizon(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    time_received = models.DateTimeField(auto_now_add=True)
    roll = models.FloatField()
    pitch = models.FloatField()
    accel = models.FloatField()
