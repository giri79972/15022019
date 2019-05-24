__author__ = 'Giri'
from django import forms
from .models import AddressData
class AddressForm(forms.ModelForm):
    class Meta:
        model=AddressData
        #fields=['name','loc','email','number']
        fields='__all__'