from django.db import models

class Api(models.Model):
     id = models.UUIDField(primary_key=True)
     sender= models.CharField(max_length=200)
     msg_type= models.CharField(max_length=200)
     receiver= models.CharField(max_length=200)
     frequency= models.IntegerField()
