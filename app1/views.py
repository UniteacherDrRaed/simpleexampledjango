from django.shortcuts import render
from .models import Doctor
# Create your views here.

def index(request):
    doctors = Doctor.objects.all()
    context = {'doctors':doctors}
    return render(request,'app1/index.html', context)
