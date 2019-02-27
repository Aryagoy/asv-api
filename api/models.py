from django.db import models
from uuid import uuid4
import datetime

class Graph(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    sender= models.CharField(max_length=200)
    msg_type= models.CharField(max_length=200)
    receiver= models.CharField(max_length=200)
    frequency= models.FloatField()
    time_received = models.DateTimeField(auto_now_add=True)

    def get_duration(self):
        return (datetime.datetime.now() - self.time_received).total_seconds()


#{'message': "{  'header': {    'stamp': {      'seconds': '1551302571',      'nanos': 171304941    },    'frameId': 'imu',    'sender': 'pub_asvprotobuf.sensor_pb2.Serial374eeadf-b7c9-41f9-8460-d9d99c425085'  },  'data': 'roll di. pitch di. yaw di. accelp di. gyrop di. temperature di.\\nroll = -25.278265\\npitch = -9.174711\\nyaw = 340.789093\\naccelp = 00-- 159.886688\\n01-- -421.907837\\n02-- 897.152344\\ngyrop = 00-- 0.000000e+00\\n01-- 0.000000e+00\\n02-- 0.000000e+00\\ntemperature = 35.875000'}"}
class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    message = models.TextField()
    level = models.IntegerField()
    name = models.CharField(max_length=200)
