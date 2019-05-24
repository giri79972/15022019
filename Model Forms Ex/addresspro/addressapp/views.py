from django.shortcuts import render
from .forms import AddressForm
from django.http.response import HttpResponse
# Create your views here.

def addressview(request):
    if request.method=='POST':
        aform=AddressForm(request.POST)
        if aform.is_valid():
            aform.save()
            return HttpResponse('Data Saved')
        else:
            return HttpResponse('Form is Invalid')
    else:
        aform=AddressForm()
        return render(request,'address.html',{'aform':aform})
