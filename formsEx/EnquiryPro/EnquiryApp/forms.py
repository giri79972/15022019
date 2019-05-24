__author__ = 'Giri'
from django import forms
from multiselectfield import MultiSelectFormField
class EnquiryForm(forms.Form):
    fname=forms.CharField(label='Enter Your Name',widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Your Name'}))
    femail=forms.EmailField(label='Enter Your Email',widget=forms.EmailInput(attrs={'class':'form_control','placeholder':'Your Email'}))
    fmobile=forms.IntegerField(label='Enter Your Mobile Number',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Your Number'}))
    COURSES_CHOICES=(
        ('py','PYTHON'),
        ('dj','DJANGO'),
        ('ui','UI'),
        ('ra','RESTAPI')
    )
    fcourse=MultiSelectFormField(max_length=500,choices=COURSES_CHOICES)
    TRAINERS_CHOICES=(
        ('RAMYA','ramya'),
        ('SAI','sai'),
        ('KESAV','kesav')
    )
    ftrainer=MultiSelectFormField(max_length=500,choices=TRAINERS_CHOICES)
    BRANCHES_CHOICES=(
        ('srnagar','SRNAGAR'),
        ('madpur','MADHAPUR'),
        ('kphb','KPHB')
    )
    fbranch=MultiSelectFormField(max_length=500,choices=BRANCHES_CHOICES)
    GENDER_CHOICES=(
        ('Male','male'),
        ('Female','female')
    )
    fgender=forms.ChoiceField(widget=forms.RadioSelect(),choices=GENDER_CHOICES)
    years=range(1960,2021,1)
    fdate=forms.DateField(widget=forms.SelectDateWidget(years=years))