from django.db import models


# Create your models here.
class bio(models.Model):
    Name = models.CharField(max_length=30,null=True)
    DOB = models.DateField(null=True)
    Age = models.IntegerField(null=True)
    Gender = models.TextField(null=True)
    Phone = models.IntegerField(null=True)
    Email = models.TextField(null=True)
    Address = models.TextField(null=True)
    Department = models.TextField(null=True)
    Material = models.TextField(null=True)
