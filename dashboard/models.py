from django.db import models
from uuid import uuid4

# Create your models here.
class Horizon(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    time_received = models.DateTimeField(auto_now_add=True)
    roll = models.FloatField()
    pitch = models.FloatField()
    accel = models.FloatField()

class Scan(models.Model):
    start_angle = models.FloatField()
    stop_angle = models.FloatField()
    angle_increment = models.FloatField()
    range_min = models.FloatField()
    range_max = models.FloatField()
    ranges = models.TextField()
    intensities = models.TextField()
