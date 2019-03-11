from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Project
from django.shortcuts import render, get_object_or_404
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'website/index.html')
    
def projectname(request):
    type_list=Project.objects.all()
    return render (request, 'website/projectname.html', {'type_list': type_list})

def traffic(request):
    type_list=Traffic.objects.all()
    return render (request, 'website/traffic.html', {'type_list': type_list})

def safety(request):
    type_list=Safety.objects.all()
    return render (request, 'website/safety.html', {'type_list': type_list})

def needgoodneighbor(request):
    type_list=NeedGoodNeighbor.objects.all()
    return render (request, 'website/needgoodneighbor.html', {'type_list': type_list})

def begoodneighbor(request):
    type_list=begoodneighbor.objects.all()
    return render (request, 'website/begoodneighbor.html', {'type_list': type_list})

def emergency(request):
    type_list=Emergency.objects.all()
    return render (request, 'website/emergency.html', {'type_list': type_list})

def celebrations(request):
    type_list=celebrations.objects.all()
    return render (request, 'website/celebrations.html', {'type_list': type_list})

@login_required
def newProject(request):
        #form=ProjectForm
        if request.method=='POST':
            form=ProjectForm(request.POST)
            if form.is_valid():
                post=form.save(commit=True)
                post.save()
                form=ProjectForm() 
        else: 
            form=ProjectForm() 
        return render(request, 'website/projectform.html', {'form': form})

def loginmessage(request):
    return render(request, 'website/loginmessage.html')

def logoutmessage(request):
    return render(request, 'website/logoutmessage.html')




