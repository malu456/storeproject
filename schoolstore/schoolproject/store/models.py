from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(auto_now_add=True)
    age =models.CharField(max_length=250)
    gender = models.CharField(max_length=250,null=True)
    phnum = models.CharField(max_length=250)
    mail = models.CharField(max_length=250)
    address = models.TextField()
    department = models.CharField(max_length=250)
    courses = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    mp = models.CharField(max_length=250)