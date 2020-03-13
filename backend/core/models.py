from django.db import models

class Car(models.Model):
    vendor = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    volume = models.PositiveIntegerField()
    class Meta:
        unique_together = [("model")]

class Users(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    telephone = models.PositiveSmallIntegerField()
    password = models.CharField(max_length=128)
    class Meta:
        unique_together = [("telephone"),("email")]

