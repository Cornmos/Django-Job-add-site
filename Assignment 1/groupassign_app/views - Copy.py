from django.shortcuts import render
from groupassign_app.catalogue import *

def home(request):
    return render(request,'groupassign_app/home.html')

def list(request):
    return render(request, 'groupassign_app/list.html', {'subjectCatalogue':subjectCatalogue})

def details(request, subjectId):
    return render(request,'groupassign_app/details.html',{'subjectId':subjectId, 'subjectCatalogue':subjectCatalogue})

def model_description(request):
    return render(request,'groupassign_app/model_description.html')
