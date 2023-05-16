from django.db import models

# Create your models here.
class Student(models.Model):
  fName = models.CharField(max_length=255)
  lName = models.CharField(max_length=255)


class Course(models.Model):
  cName = models.CharField(max_length=255)
  isFinished = models.BooleanField()