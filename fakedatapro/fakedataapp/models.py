from django.db import models

# Create your models here.

class FakeData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    sal = models.IntegerField()
    loc = models.CharField(max_length=50)
    job = models.CharField(max_length=50)