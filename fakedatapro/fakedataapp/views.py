from django.shortcuts import render,redirect
from .models import FakeData
import faker
fake = faker.Faker()

def inserting(request):
    for i in range(500):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        sal = fake.random_element(elements=(1000,2000,1500,3000))
        loc =  fake.random_element(elements=('Hyd','Bang','Pune','Mumbai'))
        job = fake.random_element(elements=('HR','SW','SM','PM'))

        data = FakeData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            sal=sal,
            loc=loc,
            job=job
        )
        data.save()
    return redirect('/home/')

def fetching(request):
    fdata = FakeData.objects.all()
    return render(request,'fakedata.html',{'fdata':fdata})