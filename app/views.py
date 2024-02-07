from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from app.forms import *
from django.views.generic import View,TemplateView
# Return HttpResponse by using Function Based View

def fbv(request):
    return HttpResponse('<h1>This string is created by using Function Based View</h1>')

# Return HttpResponse by using Class Based View

class Cbv(View):
    def get(self,request):
        return HttpResponse('<h1>This string is created by using Class Based View</h1>')
    

# Inserting Data into School Model by using Function Based View
    
def insert_school_by_fbv(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}
    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is inserted successfully')
    return render(request,'insert_school_by_fbv.html',d)

# Inserting Data into School by using Class Based View

class InsertSchoolByCbv(View):
    def get(self,request):
        ESFO = SchoolForm()
        d = {'ESFO':ESFO}
        return render(request,'InsertSchoolByCbv.html',d)
    
    def post(self,request):
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Inserted into School Model successfully')
        

class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'
    