from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class EnquiryData(models.Model):
    mname=models.CharField(max_length=20)
    memail=models.EmailField(max_length=20)
    mmobile=models.BigIntegerField()

    COURSES_CHOICES=(
        ('py','PYTHON'),
        ('dj','DJANGO'),
        ('ui','UI'),
        ('ra','RESTAPI')
    )
    mcourse=MultiSelectField(max_length=200,choices=COURSES_CHOICES)
    TRAINERS_CHOICES=(
        ('RAMYA','ramya'),
        ('SAI','sai'),
        ('KESAV','kesav')
    )
    mtrainer=MultiSelectField(max_length=200,choices=TRAINERS_CHOICES)
    BRANCHES_CHOICES=(
        ('srnagar','SRNAGAR'),
        ('madpur','MADHAPUR'),
        ('kphb','KPHB')
    )
    mbranch=MultiSelectField(max_length=200,choices=BRANCHES_CHOICES)
    GENDER_CHOICES=(
        ('Male','male'),
        ('Female','female')
    )
    mgender=models.CharField(max_length=30,choices=GENDER_CHOICES)
    mdate=models.DateField(max_length=100)