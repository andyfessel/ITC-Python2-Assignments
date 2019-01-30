from django.shortcuts import render
from .models import Resource
##from django.utils import timezone
##from .models import club
# Create your views here.
def index(request):
    return render(request, 'club/index.html')
def restype(request):
    type_list=Resource.objects.all()
    return render (request, 'club/type.html', {'type_list': type_list})

