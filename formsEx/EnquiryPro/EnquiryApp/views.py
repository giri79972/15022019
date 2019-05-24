from django.shortcuts import render

# Create your views here.
from .forms import EnquiryForm
from .models import EnquiryData
def enquiryview(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            vname=eform.cleaned_data.get('fname')
            vemail=eform.cleaned_data.get('femail')
            vmobile=eform.cleaned_data.get('fmobile')
            vcourse=eform.cleaned_data.get('fcourse')
            vtrainer=eform.cleaned_data.get('ftrainer')
            vbranch=eform.cleaned_data.get('fbranch')
            vgender=eform.cleaned_data.get('fgender')
            vdate=eform.cleaned_data.get('fdate')
            vdata=EnquiryData(
                mname=vname,
                memail=vemail,
                mmobile=vmobile,
                mcourse=vcourse,
                mtrainer=vtrainer,
                mbranch=vbranch,
                mgender=vgender,
                mdate=vdate
            )
            vdata.save()
            eform=EnquiryForm()
            return render(request,'enquiryform.html',{'eform':eform})
    else:
        eform=EnquiryForm()
        return render(request,'enquiryform.html',{'eform':eform})
