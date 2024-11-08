from django.db import models

# Create your models here.
class Student(models.Model):
    age= models.IntegerField()
    name = models.CharField(max_length=100)

class Instructor(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()

