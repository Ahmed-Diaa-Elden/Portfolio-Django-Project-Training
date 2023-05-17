from django.db import models

# Create your models here.
class Student(models.Model):
  fName = models.CharField(max_length=255)
  lName = models.CharField(max_length=255)

class Course(models.Model):
  cName = models.CharField(max_length=255)
  isFinished = models.BooleanField()

# model named Post
class Contact(models.Model):
  Male = 'M'
  FeMale = 'F'
  # this is tuple dataType
  GENDER_CHOICES = ( (Male, 'Male'), (FeMale, 'Female'), )
  # deﬁne a username ﬁeld with bound max length it can have
  name = models.CharField( max_length = 50, blank = False, null = False) # Note: when you enter empty string it takes this value "" but if you create new cell and didn't give it any data event empty data then this is null such as add new columns in table after saving data in database
  # This is used to write a post
  number = models.CharField( max_length = 20, blank = False, null = False)
  # Values for gender are restricted by giving choices
  gender = models.CharField(max_length = 6, choices = GENDER_CHOICES,  default = Male)
