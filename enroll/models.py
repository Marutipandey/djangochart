from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    firstName = models.CharField(max_length=150)  # Corrected 'max_lenth' to 'max_length'
    dateField = models.DateTimeField()
    image = models.ImageField(upload_to='images/')  # 'images/' is the directory where images will be stored
    gender = models.CharField( max_length=100,null=True,blank=True)
    course = models.CharField(max_length=100,null=True,blank=True)