from django.db import models

# Create your models here.
class CustomerData(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_mobile = models.BigIntegerField()
    customer_email = models.EmailField(max_length=50)
    customer_age = models.IntegerField()
    customer_sales = models.IntegerField()
    customer_location = models.CharField(max_length=100)
