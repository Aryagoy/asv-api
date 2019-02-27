from django.db import models
from uuid import uuid4
import datetime

class Graph(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    sender= models.CharField(max_length=200)
    msg_type= models.CharField(max_length=200)
    receiver= models.CharField(max_length=200)
    frequency= models.FloatField()
    time_received = models.DateTimeField(editable=False)

    def get_duration(self):
        return (datetime.datetime.now() - self.time_received).total_seconds()
