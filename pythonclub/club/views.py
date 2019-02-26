from django.shortcuts import render

##??? from django.http import HttpResponseRedirect
## Django Book Form directions suggest adding this line - not sure necessary

from .models import Resource
from .models import Meeting
from .forms  import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required
##from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'club/index.html')
def restype(request):
    type_list=Resource.objects.all()
    return render (request, 'club/type.html', {'type_list': type_list})
def meetingtitle(request):
    type_list=Meeting.objects.all()
    return render (request, 'club/meetinghistory.html', {'type_list': type_list})
def meetingid(request):
    type_list=Meeting.objects.all()
    return render (request, 'club/meetingid.html', {'type_list': type_list})
##Form View
@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm() 
    else: 
        form=MeetingForm() 
    return render(request, 'club/meetingform.html', {'form': form})
    
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm() 
    else: 
        form=ResourceForm() 
    return render(request, 'club/resourceform.html', {'form': form})

def loginmessage(request):
     return render(request, 'club/loginmessage.html')

def logoutmessage(request):
     return render(request, 'club/logoutmessage.html')