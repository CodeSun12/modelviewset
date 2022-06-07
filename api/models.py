from django.db import models
import rest_framework


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    city = models.CharField(max_length=100)
