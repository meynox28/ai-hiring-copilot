from django.db import models
class Job(models.Model):
    title=models.CharField(max_length=200)
    descrip=models.TextField()
    numbs=models.IntegerField()
    Date=models.DateField()
    =models.BooleanField()
# Create your models here.
