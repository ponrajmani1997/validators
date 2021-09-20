from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def forms(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse('validated')

    return render(request,'student.html',context={'form':form})