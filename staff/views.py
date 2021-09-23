from django.shortcuts import render
from staff.models import *
from django.contrib import messages

# Create your views here.

def token(request):
    if request.method == 'POST':
        cn = request.POST['CenterNameAddr']
        an = request.POST['ApplicantName']
        amn = request.POST['ApplicantMobileNo']
        at = request.POST['ApplicationType']
        ic = request.POST['inputCard']
        ich = request.POST['inpCharges']
        # print(cn,an,amn,ct,ic,ich)
        ins = staffdb(centername=cn,applicantname=an,applicantmobileno=amn,applicationtype=at,orderpvccard=ic,totalcharges=ich)
        ins.save()
        messages.success(request, "Your form has been submitted successfully...!!")
        print("Your Data Has Been Submitted Successfully")
        staff = slotbooking.objects.all() 
    return render(request, 'staff/token.html')

# def gettokendata(request):
#     staff = slotbooking.objects.all()
#     return render(request, 'staff/token.html', {'staffdata':staff})

# def staff(request):
#     return render(request, 'staff/staff.html')
