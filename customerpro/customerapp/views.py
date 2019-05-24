from django.shortcuts import render

# Create your views here.
from .models import CustomerData
def customerview(request):
    if request.method =="POST":
        cname = request.POST.get('cname','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        age = request.POST.get('age','')
        sales = request.POST.get('sales','')
        loc = request.POST.get('loc','')

        data = CustomerData(
            customer_name=cname,
            customer_mobile=mobile,
            customer_email=email,
            customer_age=age,
            customer_sales=sales,
            customer_location=loc
        )
        data.save()
        return render(request,'customer.html')
    return render(request,'customer.html')