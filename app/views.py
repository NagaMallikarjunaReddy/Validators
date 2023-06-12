from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def student(request):
    sfo=Studentform()
    d={'sfo':sfo}
    if request.method=='POST':
        sfd=Studentform(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
        else:
            return HttpResponse('<h1>data is not valid</h1>')
    return render(request,'student.html',d)