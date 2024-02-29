from django.db import models

# Create your models here.

class Server(models.Model):
    nombre = models.models.CharField(max_length=30)
    cpu = models.FloatField()
    real_memory = models.FloatField()
    virtual_memory = models.FloatField()
    disck_space = models.FloatField()