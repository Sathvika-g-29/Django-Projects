from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField(default=2002)
    email=models.CharField(max_length=100)
    